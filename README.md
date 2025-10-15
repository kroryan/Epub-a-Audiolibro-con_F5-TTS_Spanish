# eBook a Audiolibro con F5-TTS (Español)

Este repositorio convierte eBooks en audiolibros usando el modelo F5-TTS afinado para español.

Este fork incluye ajustes y correcciones para usar el modelo español de `jpgallegoar/F5-Spanish` y soluciónes específicas para entornos Windows con GPU NVIDIA (por ejemplo, RTX 5060 Ti).

Resumen rápido
- Modelo: jpgallegoar/F5-Spanish (model_1200000.safetensors usado por defecto aquí)
- Vocabulario: `spanish_vocab.txt` (vocab del modelo)
- Interfaz: Gradio (app.py)

Cambios importantes en este fork
- Desactivada la conversión automática de texto a pinyin en `f5_tts_working_code/infer/utils_infer.py` para que el sistema funcione correctamente con texto en español.
- Añadida lógica para forzar el uso de `spanish_vocab.txt` si está presente en la raíz del proyecto.
- Parámetros del modelo ajustados en `app.py` para coincidir con la arquitectura del modelo español (dim=1024, depth=22, heads=16, ff_mult=2, text_dim=512, conv_layers=4).

Licencia y creditos
- Basado en el proyecto original F5-TTS de SWivid y el modelo finetuneado de jpgallegoar.
# Easy eBook to Audiobook Converter with F5-TTS

![image](https://github.com/user-attachments/assets/d286b6e4-7a73-4e9d-88af-dc910652d743)

0. 
    # eBook a Audiolibro con F5-TTS (Español)

    Convierte eBooks en audiolibros usando el modelo F5-TTS afinado para español.

    Este fork está pensado para entornos Windows con GPU NVIDIA (por ejemplo, RTX 5060 Ti) y contiene correcciones para asegurar una síntesis coherente en español.

    Resumen rápido
    - Modelo por defecto: `jpgallegoar/F5-Spanish` (se recomienda `model_1200000.safetensors` en este repositorio)
    - Vocabulario: `spanish_vocab.txt` (vocab del modelo)
    - Interfaz: Gradio (archivo `app.py`)

    Cambios importantes en este fork
    - Se desactivó la conversión automática de caracteres a pinyin en `f5_tts_working_code/infer/utils_infer.py` para evitar que el texto español se convierta a pinyin chino.
    - Se añadió detección automática y uso de `spanish_vocab.txt` en la raíz del proyecto si existe.
    - Se ajustaron y forzaron los parámetros del modelo en `app.py` para coincidir con la arquitectura del modelo español (dim=1024, depth=22, heads=16, ff_mult=2, text_dim=512, conv_layers=4).

    Requisitos mínimos
    - Python 3.11
    - GPU NVIDIA con drivers compatibles (se probó en RTX 5060 Ti con CUDA 12.8)
    - ffmpeg en PATH

    Instalación rápida (PowerShell)

    ```powershell
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    pip install python-magic-bin       # Windows: si falla python-magic
    pip install torchcodec             # Opcional, si hay problemas con torchaudio/TorchCodec
    ```

    Instalar PyTorch (ejemplo para CUDA 12.8)

    ```powershell
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
    ```

    Descargar modelo y vocabulario
    - Descarga `model_1200000.safetensors` desde `jpgallegoar/F5-Spanish` y ponlo en la caché de Hugging Face o en la ruta mostrada por `app.py` al arrancar.
    - Descarga `vocab.txt` desde el mismo repositorio y guárdalo como `spanish_vocab.txt` en la raíz del proyecto.

    Ejecutar la aplicación

    ```powershell
    $env:GRADIO_SERVER_PORT="7861"; python app.py
    ```

    Abre en el navegador: `http://localhost:7861`.

    Uso recomendado
    - Sube una muestra de voz en español (<=15s) con buena calidad.
    - Proporciona la transcripción en español (esto mejora la clonación de voz).

    Créditos
    - Fork basado en el proyecto original F5-TTS (SWivid).
    - Modelo finetuneado para español por `jpgallegoar` (jpgallegoar/F5-Spanish).
    - Este fork por `kroryan` contiene ajustes y documentación en español.

    Licencia
    - Respeta las licencias de los proyectos originales y del modelo (revisa la página del modelo en Hugging Face para detalles).

    Agradecimientos
    - Gracias a SWivid por el proyecto base F5-TTS y a jpgallegoar por el modelo español. y al creador original de este repositorio
