FROM node:lts

WORKDIR /usr/angular
RUN npm install -g @angular/cli

COPY package.json .
RUN npm install

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

COPY . .
EXPOSE 4200
CMD ng serve --host 0.0.0.0
