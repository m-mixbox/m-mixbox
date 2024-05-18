<?php 
include('config/db.php');
          
          $sql = "SELECT * From users ";
          $query = mysqli_query($connection, $sql);
          $row = mysqli_fetch_array($query);
          echo "ID= "; echo $row[0];
?>