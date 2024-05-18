<?php     
    session_start();
    session_destroy();
      
    header("Location: http://localhost/scripts/php-user-authentication/index.php")
;?>