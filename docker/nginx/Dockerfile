FROM node:14.15.1 as build-stage
WORKDIR /frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend ./
RUN npm run build

FROM nginx:latest as prod-stage
COPY ./docker/nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build-stage /frontend/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]