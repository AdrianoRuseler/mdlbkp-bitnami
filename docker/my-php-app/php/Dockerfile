FROM php:8.3-fpm-alpine

# Install system dependencies
RUN apk add --no-cache \
    postgresql-dev \
    libpng-dev \
    libjpeg-turbo-dev \
    freetype-dev \
    zip \
    libzip-dev \
    oniguruma-dev \
    curl-dev \
    icu-dev \
    libxml2-dev

# Install PHP extensions
RUN docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j$(nproc) \
        pdo \
        pdo_pgsql \
        pgsql \
        gd \
        zip \
        intl \
        opcache \
        bcmath \
        soap \
        mbstring \
        xml \
        curl

# Install Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Set working directory
WORKDIR /var/www/html

# Copy PHP configuration
COPY php.ini /usr/local/etc/php/php.ini

# Create user and group
RUN addgroup -g 1000 -S www && \
    adduser -u 1000 -S www -G www

# Change ownership of working directory
RUN chown -R www:www /var/www/html

# Switch to non-root user
USER www

# Expose port 9000
EXPOSE 9000

CMD ["php-fpm"]