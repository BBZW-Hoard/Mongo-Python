FROM node:18 as builder
RUN npm i -g --save @vue/cli
WORKDIR /src/vue
COPY package* /src/vue/
RUN chown -R node:node /src
USER node
RUN npm install
COPY . /src/vue/
RUN npm run build
CMD [ "npm", "run", "serve" ]

FROM nginx:alpine
WORKDIR /usr/share/nginx/html
COPY --from=builder /src/vue/dist/ .
COPY default.conf /etc/nginx/conf.d/
RUN touch /var/run/nginx.pid && \
    chown -R nginx:nginx /var/run/nginx.pid

EXPOSE 8080

