FROM rust:alpine

WORKDIR /usr/src/hunter_diary

COPY . .

RUN cargo test && cargo install --path . && cargo build

CMD ["hunter_diary"]
