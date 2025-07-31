<?php
// Database connection example
$host = $_ENV['DB_HOST'] ?? 'postgres';
$port = $_ENV['DB_PORT'] ?? '5432';
$dbname = $_ENV['DB_NAME'] ?? 'myapp';
$username = $_ENV['DB_USER'] ?? 'myuser';
$password = $_ENV['DB_PASSWORD'] ?? 'mypassword';

try {
    $dsn = "pgsql:host=$host;port=$port;dbname=$dbname";
    $pdo = new PDO($dsn, $username, $password, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);
    
    $db_status = "✅ PostgreSQL connection successful";
    
    // Test query
    $stmt = $pdo->query("SELECT version() as version");
    $db_version = $stmt->fetch()['version'];
    
} catch (PDOException $e) {
    $db_status = "❌ Database connection failed: " . $e->getMessage();
    $db_version = "N/A";
}

phpinfo();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP-FPM + Nginx + PostgreSQL Docker Environment</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            border-bottom: 3px solid #007acc;
            padding-bottom: 10px;
        }
        .status {
            background: #e8f5e8;
            border: 1px solid #4caf50;
            padding: 15px;
            border-radius: 5px;
            margin: 15px 0;
        }
        .error {
            background: #ffeaea;
            border: 1px solid #f44336;
        }
        .info-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-top: 20px;
        }
        .info-box {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #007acc;
        }
        .info-box h3 {
            margin-top: 0;
            color: #007acc;
        }
        pre {
            background: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
            white-space: pre-wrap;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🐳 Docker Environment Status</h1>
        
        <div class="status <?= strpos($db_status, '❌') !== false ? 'error' : '' ?>">
            <strong>Database Status:</strong> <?= htmlspecialchars($db_status) ?>
        </div>

        <div class="info-grid">
            <div class="info-box">
                <h3>🐘 PHP Information</h3>
                <p><strong>Version:</strong> <?= PHP_VERSION ?></p>
                <p><strong>SAPI:</strong> <?= php_sapi_name() ?></p>
                <p><strong>Memory Limit:</strong> <?= ini_get('memory_limit') ?></p>
                <p><strong>Max Execution Time:</strong> <?= ini_get('max_execution_time') ?>s</p>
            </div>

            <div class="info-box">
                <h3>🗄️ PostgreSQL Information</h3>
                <p><strong>Host:</strong> <?= htmlspecialchars($host) ?></p>
                <p><strong>Port:</strong> <?= htmlspecialchars($port) ?></p>
                <p><strong>Database:</strong> <?= htmlspecialchars($dbname) ?></p>
                <p><strong>Version:</strong> <?= isset($db_version) ? htmlspecialchars(substr($db_version, 0, 50)) . '...' : 'N/A' ?></p>
            </div>

            <div class="info-box">
                <h3>🌐 Server Information</h3>
                <p><strong>Server Software:</strong> <?= $_SERVER['SERVER_SOFTWARE'] ?? 'N/A' ?></p>
                <p><strong>Document Root:</strong> <?= $_SERVER['DOCUMENT_ROOT'] ?? 'N/A' ?></p>
                <p><strong>Server Name:</strong> <?= $_SERVER['SERVER_NAME'] ?? 'N/A' ?></p>
                <p><strong>Request Time:</strong> <?= date('Y-m-d H:i:s', $_SERVER['REQUEST_TIME']) ?></p>
            </div>

            <div class="info-box">
                <h3>🔧 PHP Extensions</h3>
                <p><strong>PDO:</strong> <?= extension_loaded('pdo') ? '✅' : '❌' ?></p>
                <p><strong>PDO PostgreSQL:</strong> <?= extension_loaded('pdo_pgsql') ? '✅' : '❌' ?></p>
                <p><strong>GD:</strong> <?= extension_loaded('gd') ? '✅' : '❌' ?></p>
                <p><strong>Curl:</strong> <?= extension_loaded('curl') ? '✅' : '❌' ?></p>
                <p><strong>Zip:</strong> <?= extension_loaded('zip') ? '✅' : '❌' ?></p>
                <p><strong>OPcache:</strong> <?= extension_loaded('opcache') ? '✅' : '❌' ?></p>
            </div>
        </div>

        <div style="margin-top: 30px; text-align: center; color: #666;">
            <p>🎉 Your PHP-FPM + Nginx + PostgreSQL Docker environment is ready!</p>
            <p><a href="http://localhost:8080" target="_blank">📊 Access pgAdmin</a> (admin@example.com / admin)</p>
        </div>
    </div>
</body>
</html>