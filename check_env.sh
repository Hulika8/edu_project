#!/bin/bash

echo "=== Virtual Environment Kontrol Scripti ==="
echo ""

# Virtual Environment Kontrolü
if [ -n "$VIRTUAL_ENV" ]; then
    echo "✅ Virtual Environment Aktif: $VIRTUAL_ENV"
else
    echo "❌ Virtual Environment Aktif Değil"
    echo "Çözüm: source env/bin/activate"
fi

echo ""

# Python Kontrolü
if command -v python &> /dev/null; then
    echo "✅ Python Bulundu: $(which python)"
    echo "   Versiyon: $(python --version)"
else
    echo "❌ Python Bulunamadı"
fi

echo ""

# Django Kontrolü
if python -c "import django" &> /dev/null; then
    echo "✅ Django Kurulu: $(python -c 'import django; print(django.get_version())')"
else
    echo "❌ Django Kurulu Değil"
    echo "Çözüm: pip install django"
fi

echo ""

# Cursor Ayarları Kontrolü
if [ -f ".vscode/settings.json" ]; then
    echo "✅ Cursor Ayarları Mevcut: .vscode/settings.json"
else
    echo "❌ Cursor Ayarları Bulunamadı"
fi

echo ""

# Shell Ayarları Kontrolü
if grep -q "smartedu_project" ~/.zshrc; then
    echo "✅ Shell Ayarları Mevcut: ~/.zshrc"
else
    echo "❌ Shell Ayarları Bulunamadı"
fi

echo ""
echo "=== Kontrol Tamamlandı ==="
