FROM push argovis/rust:base

WORKDIR /app
COPY . .
RUN chown -R 1000660000 /app
CMD bash run.sh
