# Optimizacion de imagenes

Ejecutar UNA VEZ desde la carpeta del proyecto. Requiere Node 18+.

```bash
npm install --no-save sharp
node -e "
const sharp=require('sharp'), fs=require('fs'), path=require('path');
const walk=d=>fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>{
  const p=path.join(d,e.name);
  return e.isDirectory()?walk(p):(/\.(jpe?g|png)$/i.test(e.name)?[p]:[]);
});
let n=0;
for (const f of walk('assets')) {
  if (/certifications|logo|favicon|apple-touch/i.test(f)) continue;
  const out=f.replace(/\.(jpe?g|png)$/i,'.webp');
  sharp(f).resize({width:1600,withoutEnlargement:true}).webp({quality:78})
    .toFile(out).then(()=>console.log('OK',out)).catch(e=>console.error('ERR',f,e.message));
  n++;
}
console.log('Procesando',n,'imagenes');
"
```

Despues de ejecutarlo, confirmar que cada `.jpg`/`.jpeg` tiene su `.webp` al lado.