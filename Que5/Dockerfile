FROM node:alpine
WORKDIR /usr/Program/publisher
COPY publisher.js /usr/Program/publisher/
COPY data.json /usr/Program/publisher/
RUN npm install mqtt
CMD ["node", "publisher.js"]