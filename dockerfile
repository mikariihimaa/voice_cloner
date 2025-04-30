FROM ghcr.io/coqui-ai/tts-cpu:latest

# Päivitä apt ja asenna tarvittavat paketit (esim. ALSA-tuki, jos tarvitaan ääntä myöhemmin)
RUN apt-get update && apt-get install -y alsa-utils

# Asenna Flask
RUN pip install Flask

# Luo hakemisto sovellukselle
WORKDIR /app

# Kopioi sovellustiedostot
COPY app.py /app/
COPY templates /app/templates/

# Altistetaan Flaskin portti
EXPOSE 5002

# Käynnistä sovellus
CMD ["python3", "app.py"]
 
