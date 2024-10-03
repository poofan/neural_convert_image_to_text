# Шаг 1: Сборка Angular приложения
FROM node:20 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build --prod

# Шаг 2: Сервировка с помощью Node.js
FROM node:20
WORKDIR /app
COPY --from=build /app/dist/image-upload-app /app
RUN npm install -g serve
EXPOSE 5000
CMD ["serve", "-s", ".", "-l", "5000"]
