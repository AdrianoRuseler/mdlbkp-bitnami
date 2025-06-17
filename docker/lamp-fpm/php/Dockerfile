FROM php:8.3-fpm

# Install dependencies and mysqli
RUN apt-get update && apt-get install -y \
    libpng-dev \
    libjpeg-dev \
    libfreetype6-dev \
    libonig-dev \
    libxml2-dev \
    libzip-dev \
    unzip \
    && docker-php-ext-install mysqli pdo pdo_mysql

# Optional: clean up to keep the image small
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Optional: set working directory
WORKDIR /var/www/html
