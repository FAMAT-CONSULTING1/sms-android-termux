# Ejecución automática de curl cada 5 minutos en Termux

## 1. Crear el archivo

```bash
nano sync.sh
```

---

## 2. Pegar este contenido

```bash
#!/data/data/com.termux/files/usr/bin/bash

while true; do
  curl -X POST http://127.0.0.1:8000/sync
  sleep 300
done
```

---

## 3. Guardar el archivo

En nano:

- CTRL + O → Enter
- CTRL + X

---

## 4. Dar permisos de ejecución

```bash
chmod +x sync.sh
```

---

## 5. Ejecutar el script

```bash
./sync.sh
```

---

## 6. Ejecutarlo en segundo plano (opcional)

```bash
nohup ./sync.sh > sync.log 2>&1 &
```

Ver procesos activos:

```bash
ps aux | grep sync.sh
```

Detener proceso:

```bash
pkill -f sync.sh
```

---

## 7. Ver logs (opcional)

```bash
cat sync.log
```

Ver logs en tiempo real:

```bash
tail -f sync.log
```