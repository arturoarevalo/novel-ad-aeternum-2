import { writeFileSync, mkdirSync, readFileSync } from "node:fs";
import { run as build } from "./build";
import { Proyecto } from "./lib/Proyecto";
import { existe, c } from "./lib/util";

function mdAHtmlMuySimple(md: string): string {
  // Conversión deliberadamente mínima (es un stub de previsualización).
  const escapar = (s: string) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  const lineas = md.split("\n");
  const out: string[] = [];
  for (const l of lineas) {
    if (/^#\s+/.test(l)) out.push(`<h1>${escapar(l.replace(/^#\s+/, ""))}</h1>`);
    else if (/^##\s+/.test(l)) out.push(`<h2>${escapar(l.replace(/^##\s+/, ""))}</h2>`);
    else if (/^###\s+/.test(l)) out.push(`<h3>${escapar(l.replace(/^###\s+/, ""))}</h3>`);
    else if (/^>\s?/.test(l)) out.push(`<blockquote>${escapar(l.replace(/^>\s?/, ""))}</blockquote>`);
    else if (l.trim() === "---") out.push("<hr>");
    else if (l.trim() === "") out.push("");
    else out.push(`<p>${escapar(l)}</p>`);
  }
  return `<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Previsualización</title>
<style>body{max-width:42rem;margin:3rem auto;padding:0 1rem;font:1.05rem/1.7 Georgia,serif;color:#1a1a1a}
h1,h2,h3{font-family:system-ui,sans-serif;line-height:1.2}blockquote{color:#555;font-style:italic;border-left:3px solid #ddd;padding-left:1rem}
hr{border:0;border-top:1px solid #e5e5e5;margin:2.5rem 0}</style></head><body>
${out.join("\n")}
</body></html>`;
}

export function run(_args: string[]): number {
  const proyecto = new Proyecto();
  const meta = proyecto.metadatos();

  build([]); // asegura builds/<slug>.md actualizado
  const mdPath = proyecto.ruta("builds", `${meta.slug}.md`);
  if (!existe(mdPath)) {
    console.error(c.rojo("deploy: no hay build que publicar."));
    return 1;
  }
  const md = readFileSync(mdPath, "utf8");
  const html = mdAHtmlMuySimple(md);

  mkdirSync(proyecto.ruta("builds"), { recursive: true });
  const htmlPath = proyecto.ruta("builds", `${meta.slug}.html`);
  writeFileSync(htmlPath, html, "utf8");

  // --- STUB de subida: aquí irá la integración real (S3, Netlify, etc.) ---
  const urlFalsa = `https://preview.local/${meta.slug}/${Date.now().toString(36)}`;
  writeFileSync(
    proyecto.ruta("builds", `${meta.slug}.deploy.json`),
    JSON.stringify({ slug: meta.slug, html: `builds/${meta.slug}.html`, url: urlFalsa, ts: new Date().toISOString() }, null, 2),
    "utf8"
  );

  console.log(c.verde("✔ deploy (simulado):"));
  console.log(`  html:    ${htmlPath}`);
  console.log(`  url:     ${c.azul(urlFalsa)}  ${c.gris("(stub — sustituir por subida real)")}`);
  return 0;
}
