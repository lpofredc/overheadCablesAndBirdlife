## Build
FROM node:lts-alpine as builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN yarn
COPY . ./
RUN yarn build

FROM nginx:mainline-alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY default.conf /etc/nginx/conf.d/default.conf
