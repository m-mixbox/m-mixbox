<?php
function logAdminAction($pdo, $admin_id, $action_type, $description) {
    try {
        $sql = "INSERT INTO admin_logs (admin_id, action_type, description, ip_address) 
                VALUES (:admin_id, :action_type, :description, :ip_address)";
        $stmt = $pdo->prepare($sql);
        $stmt->execute([
            ':admin_id' => $admin_id,
            ':action_type' => $action_type,
            ':description' => $description,
            ':ip_address' => $_SERVER['REMOTE_ADDR']
        ]);
        return true;
    } catch(PDOException $e) {
        error_log("Error logging admin action: " . $e->getMessage());
        return false;
    }
}
?>