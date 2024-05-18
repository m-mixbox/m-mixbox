<?php 
    include('config/db.php'); 
    //global $email,$lastname ;
        /*$email = $_SESSION['email'];
        $sql = "SELECT * From users WHERE email = '{$email}' ";
        $data = mysqli_query($connection, $sql);
        $rowData =  mysqli_fetch_array($data);
        $id = $rowData['id'];*/
        //global $id,$lastname;
        
        $data = $_POST['id'];
        $sql = "SELECT * From users where id= '$data'";
          $query = mysqli_query($connection, $sql);
          $row = mysqli_fetch_array($query);
          echo "ID= "; echo $row[3];
        
        
        /*
        if(isset($_POST['id']))
        {$id = $_POST['id'];}
        if(isset($_POST['lastname']))
        {$lastname = $_POST['lastname'];}
        echo $_POST['id'];
        */
        
        //$sql = "UPDATE users SET lastname='{$lastname}' where id = '{$id}'";
        //if(empty($name_err) && empty($address_err) && empty($salary_err))
        //{
          // Prepare an update statement
          /*$sql = "UPDATE users SET lastname=? WHERE id=?";
           
          if($stmt = mysqli_prepare($connection, $sql))
          {
              // Bind variables to the prepared statement as parameters
              mysqli_stmt_bind_param($stmt, "sssi", $lastname, $id);
              
              // Set parameters
              //$param_lastname = $lastname;
              //$param_address = $address;
              //$param_salary = $salary;
              //$param_id = $id;
              
              // Attempt to execute the prepared statement
              if(mysqli_stmt_execute($stmt))
              {
                  // Records updated successfully. Redirect to landing page
                  header("location: temp.php");
                  exit();
              } else{
                  echo "Oops! Something went wrong. Please try again later.";
              }
            }
           
          // Close statement
          mysqli_stmt_close($stmt);
        //}
        mysqli_close($connection);
        /*if (mysqli_query($connection, $sql)) {
            echo '<div class="alert alert-success" role="alert">
            This is a success alert—check it out!
          </div>';
          } else {
            echo '<div class="alert alert-danger" role="alert">
            This is a danger alert—check it out!
          </div>';
          }
        mysqli_close($connection); */
        //$query = mysqli_query($connection, $sql);
        //$row = mysqli_fetch_array($query);
        /*$id            = $row['id'];
        $firstname     = $row['firstname'];
        $lastname      = $row['lastname'];
        $email         = $row['email'];
        $mobilenumber   = $row['mobilenumber'];
        $pass_word     = $row['password'];
        $token         = $row['token'];
        $is_active     = $row['is_active'];
        $sql2 = "SELECT * From user_data WHERE id = '{$id}' ";
        //$query2 = mysqli_query($connection, $sql2);
        //$row2 = mysqli_fetch_array($query2);
        $access_level            = $row2['access_level'];
        $phone1     = $row2['phone_no_1'];
        $phone2      = $row2['phone_no_2'];
        $phone3         = $row2['phone_no_3'];
        $pan   = $row2['pan_card'];
        $aadhar     = $row2['aadhar'];
        $address         = $row2['address'];
        $whatsapp     = $row2['whatsapp'];
        $bank            = $row2['bank_acc'];
        $name_in_bank     = $row2['name_in_bank'];
        $ifsc      = $row2['ifsc_code'];
        $email2         = $row2['email_2'];
        $position   = $row2['position'];
        $date_of_joining     = $row2['date_of_joining'];
        $contract_validity         = $row2['contract_validity'];
        $contract_period     = $row2['contract_period'];
        $district1            = $row2['district_1'];
        $district2      = $row2['district_2'];
        $district3      = $row2['district_3'];
        $email1         = $row2['email_1'];
        $district4   = $row2['district_4'];
        $district5     = $row2['district_5'];
        $state1         = $row2['state_1'];
        $state2     = $row2['state_2'];
        $state3         = $row2['state_3'];
        $state4     = $row2['state_4'];
        $state5         = $row2['state_5'];*/
?>