# Guía de Configuración: eBook to Audiobook con F5-TTS Español

Esta guía explica todos los cambios realizados para configurar el proyecto con el modelo español de F5-TTS (`jpgallegoar/F5-Spanish`) y los pasos para reproducir la instalación en otros equipos.

## Cambios Realizados en el Código

### 1. Modificación del Modelo en `app.py`

**Archivo**: `app.py`
**Línea**: 61

**Cambio Original**:
```python
ckpt_path = str(cached_path("hf://SWivid/F5-TTS/F5TTS_Base/model_1200000.safetensors"))
```

**Cambio Nuevo**:
```python
ckpt_path = str(cached_path("hf://jpgallegoar/F5-Spanish/model_1250000.safetensors"))
```

### 2. Modificación del Modelo en `preload_models.py`

**Archivo**: `preload_models.py`
**Línea**: 11

**Cambio Original**:
```python
F5TTS_MODEL_FILE = "hf://SWivid/F5-TTS/F5TTS_Base/model_1200000.safetensors" # As seen in logs
```

**Cambio Nuevo**:
```python
F5TTS_MODEL_FILE = "hf://jpgallegoar/F5-Spanish/model_1250000.safetensors" # Spanish F5-TTS model - Latest version
```

### 3. Actualización del Título de la Interfaz

**Archivo**: `app.py`
**Línea**: 553

**Cambio Original**:
```python
gr.Markdown("# eBook to Audiobook with F5-TTS!")
```

**Cambio Nuevo**:
```python
gr.Markdown("# eBook to Audiobook with F5-TTS (Spanish)!")
```

### 4. Corrección de Importaciones

**Archivo**: `app.py`
**Líneas**: 29-33

**Cambio Original**:
```python
from f5_tts.model import DiT
from f5_tts.infer.utils_infer import (
    load_vocoder,
    load_model,
    preprocess_ref_audio_text,
    infer_process,
)
```

**Cambio Nuevo**:
```python
from f5_tts_working_code.model import DiT
from f5_tts_working_code.infer.utils_infer import (
    load_vocoder,
    load_model,
    preprocess_ref_audio_text,
    infer_process,
)
```

## Pasos para Reproducir en Otros Equipos

### Requisitos Previos

1. **Python 3.8 o superior**
2. **Git** (para clonar el repositorio)
3. **Conexión a Internet** (para descargar el modelo)

### Instalación Paso a Paso

#### 1. Clonar el Repositorio
```bash
git clone https://github.com/quantumlump/eBook_to_Audiobook_with_F5-TTS.git
cd eBook_to_Audiobook_with_F5-TTS
```

#### 2. Instalar Dependencias Básicas
```bash
pip install f5-tts
pip install gradio
pip install transformers
pip install cached_path
pip install ebooklib
pip install beautifulsoup4
pip install pydub
pip install mutagen
pip install nltk
pip install soundfile
pip install magic
pip install grpcio
```

#### 3. Descargar Recursos de NLTK
```bash
python -c "import nltk; nltk.download('punkt')"
```

#### 4. Verificar las Modificaciones
Asegúrate de que los siguientes archivos contengan los cambios mencionados:

- `app.py`: Modelo cambiado a `jpgallegoar/F5-Spanish`
- `preload_models.py`: Ruta del modelo actualizada
- Importaciones corregidas para usar `f5_tts_working_code`

#### 5. Ejecutar la Aplicación
```bash
python app.py
```

### Posibles Problemas y Soluciones

#### Problema 1: Errores de CUDA
**Solución**: El proyecto debería funcionar tanto en CPU como GPU. Si hay problemas con CUDA, asegúrate de tener PyTorch instalado correctamente:
```bash
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118
```

#### Problema 2: Modelo No Se Descarga
**Síntomas**: La aplicación se cuelga al inicio
**Solución**: 
1. Esperar unos minutos (la primera descarga puede tardar)
2. Verificar conexión a internet
3. Verificar que Hugging Face esté accesible

#### Problema 3: Errores de Importación
**Solución**: Verificar que todas las dependencias estén instaladas:
```bash
pip list | grep -E "(f5-tts|gradio|transformers)"
```

#### Problema 4: Falta python-magic en Windows
```bash
pip install python-magic-bin
```

#### Problema 5: TorchCodec incompatible con PyTorch 2.9
**Síntomas**: Error "TorchCodec is required" o problemas con FFmpeg DLL
**Solución**: Usar PyTorch 2.8 compatible con TorchCodec:
```bash
pip uninstall torch torchvision torchaudio -y
pip install torch==2.8.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
pip install torchcodec
```

### Primera Ejecución

La **primera vez** que ejecutes la aplicación:

1. El modelo español se descargará automáticamente desde Hugging Face
2. Esto puede tomar **5-15 minutos** dependiendo de tu conexión
3. El modelo se almacenará en caché para usos futuros
4. Verás mensajes en la consola indicando el progreso

### Uso de la Aplicación

Una vez que la aplicación esté ejecutándose:

1. Abre tu navegador en `http://127.0.0.1:7860`
2. Sube un archivo eBook (EPUB, TXT, etc.)
3. Proporciona un audio de referencia en español
4. El sistema generará el audiolibro usando el modelo español

## Información del Modelo Español

- **Modelo**: `jpgallegoar/F5-Spanish`
- **Basado en**: F5-TTS original de SWivid
- **Idiomas soportados**: Español (múltiples acentos)
- **Datos de entrenamiento**: 218 horas de audio en español
- **Acentos incluidos**: Peninsular, Argentino, Chileno, Colombiano, Peruano, Puertorriqueño, Venezolano

## Archivos Modificados

1. `app.py` - Archivo principal de la aplicación
2. `preload_models.py` - Script de precarga de modelos
3. `GUIDE.md` - Esta guía (archivo nuevo)

## Verificación de Funcionamiento

Para verificar que todo funciona correctamente:

1. Ejecuta `python app.py`
2. Espera a que aparezca: "Running on http://127.0.0.1:7860"
3. Abre la URL en tu navegador
4. Deberías ver la interfaz con el título "eBook to Audiobook with F5-TTS (Spanish)!"

## Soporte

Si encuentras problemas:

1. Verifica que todos los pasos de instalación se completaron
2. Revisa los logs en la consola para errores específicos
3. Asegúrate de tener suficiente espacio en disco (el modelo ocupa ~1-2GB)
4. Consulta la documentación original del modelo: https://huggingface.co/jpgallegoar/F5-Spanish

---

**Nota**: Esta configuración está optimizada para generar audiolibros en español con alta calidad usando el modelo fine-tuned específicamente para el idioma español.