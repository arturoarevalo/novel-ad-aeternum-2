// Tipos compartidos del instrumental de la novela.

export type Severidad = "error" | "aviso" | "info";

export interface Hallazgo {
  regla: string;
  severidad: Severidad;
  archivo: string;
  linea: number;
  fragmento: string;
  mensaje: string;
}

export interface ResumenRegla {
  regla: string;
  total: number;
}

export interface FrontMatter {
  [clave: string]: string | string[] | number | boolean | undefined;
}

export interface DocConFrontMatter {
  fm: FrontMatter;
  cuerpo: string;
  /** Número de línea (1-based) donde empieza el cuerpo, para reportar bien. */
  lineaCuerpo: number;
}

export interface CapituloMeta {
  n: number;
  slug: string;
  titulo: string;
  archivo: string;
}

export interface Metadatos {
  titulo: string;
  subtitulo?: string;
  autor: string;
  idioma: string;
  slug: string;
  sinopsis_corta?: string;
  capitulos: CapituloMeta[];
  // Campos de publicación (Fase E, preparados pero opcionales)
  publicacion?: {
    blurb?: string;
    keywords?: string[];
    categorias?: string[];
    comp_titles?: string[];
    publico_objetivo?: string;
  };
}

export interface ReglaCoherencia {
  nombre: string;
  from: string;
  to: string;
  relacion: string;
}

export interface ConfigCoherencia {
  scan: { path: string; tipo: string }[];
  reglas: ReglaCoherencia[];
}

export interface Arista {
  fromId: string;
  toId: string;
  relacion: string;
  fromPath: string;
  toPath: string;
}
