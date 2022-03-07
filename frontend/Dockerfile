# FROM node:lts-alpine
# ENV NODE_ENV=production
# WORKDIR /usr/src/app
# COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]
# RUN npm install --production --silent && mv node_modules ../
# COPY . .
# EXPOSE 3000
# RUN chown -R node /usr/src/app
# USER node
# RUN npm run build
# CMD ["npm", "start"]

## Build
FROM node:lts-alpine as builder
WORKDIR /app
COPY package.json ./
RUN yarn
COPY . ./
RUN yarn build

# ## Prod
# FROM node:alpine
# # RUN apk update && apk upgrade && \
# #     apk add --no-cache git
# WORKDIR /app
# COPY package.json ./
# # ENV NODE_ENV=production
# RUN npm install --production
# COPY nuxt.config.js ./
# COPY --from=builder /app/.nuxt ./.nuxt/
# COPY --from=builder /app/static ./static/
# COPY --from=builder /app/content ./content/
# EXPOSE 3000
# ENV NUXT_HOST=0.0.0.0
# ENTRYPOINT [ "npm", "run" ]
# CMD [ "start" ]

FROM nginx:mainline-alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY default.conf /etc/nginx/conf.d/default.conf
