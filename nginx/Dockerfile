FROM nginx:alpine

# remove the defautl configuration of nginx
RUN rm /etc/nginx/conf.d/default.conf
# and copy our new config to nginx directory
COPY nginx.conf /etc/nginx/conf.d