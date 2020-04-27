FROM node:lts

WORKDIR /usr/webapp

COPY package.json .
COPY vue.config.js .
RUN npm install
COPY public public/
COPY src src/
EXPOSE 8080
RUN npm install -g @vue/cli
CMD ["npm","run", "serve"]
