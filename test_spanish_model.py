#!/usr/bin/env python3

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'f5_tts_working_code'))

import torch
from cached_path import cached_path
from model import DiT
from infer.utils_infer import load_model, load_vocoder

print("Testing Spanish F5-TTS model loading...")

# Test device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Test model loading
try:
    print("Loading Spanish F5-TTS model...")
    ckpt_path = str(cached_path("hf://jpgallegoar/F5-Spanish/model_1200000.safetensors"))
    print(f"Model path: {ckpt_path}")
    
    model_cfg = {
        "dim": 1024,
        "depth": 22,
        "heads": 16,
        "ff_mult": 2,
        "text_dim": 512,
        "conv_layers": 4
    }
    
    model = load_model(DiT, model_cfg, ckpt_path)
    model.eval()
    model = model.to(device)
    print(f"✓ Spanish F5-TTS model loaded successfully on {device}")
    
    # Test vocoder
    print("Loading vocoder...")
    vocoder = load_vocoder()
    print("✓ Vocoder loaded successfully")
    
    print("\n🎉 All models loaded successfully! The Spanish F5-TTS model is ready to use.")
    
except Exception as e:
    print(f"❌ Error loading models: {e}")
    import traceback
    traceback.print_exc()