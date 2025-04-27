# Use the official Node.js image from Docker Hub
FROM node:16

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to install dependencies
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose port 3000 for the application
EXPOSE 3000

# Run the app when the container starts
CMD ["node", "index.js"]
# Testing GitHub Actions workflow

