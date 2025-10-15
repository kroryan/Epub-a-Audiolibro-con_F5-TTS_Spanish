Túnel para Colab (ngrok / cloudflared)

Este documento explica cómo exponer la app Gradio que corre en Colab a una URL pública temporal usando *ngrok* o *cloudflared*. No integramos el túnel en el código del proyecto: se hace desde Colab.

1) Ngrok (requiere token)
- Regístrate en https://ngrok.com y copia tu Authtoken.
- En Colab ejecuta:

```bash
pip install pyngrok
from pyngrok import ngrok
ngrok.set_auth_token("<TU_AUTH_TOKEN>")
# Abre el tunel al puerto donde Gradio escucha, por ejemplo 7861
public_url = ngrok.connect(7861, "http").public_url
print(public_url)
```

2) cloudflared (alternativa sin pyngrok)
- Descarga y configura cloudflared:

```bash
# Linux/Colab
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64
chmod +x cloudflared-linux-amd64
./cloudflared-linux-amd64 tunnel --url http://localhost:7861
```

- cloudflared imprimirá una URL pública que redirige a `localhost:7861`.

Notas de seguridad
- Estas URLs son temporales; no expongas información sensible.
- Para uso prolongado, configura autenticación en Gradio o usa un túnel con protección.
