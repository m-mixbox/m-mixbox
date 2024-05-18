<?php
if (isset($_POST['html'])) {
    $htmlContent = $_POST['html'];

    require_once 'vendor/autoload.php'; // Include html2pdf library
    use Spipu\Html2Pdf\Html2Pdf;
    
    $html2pdf = new Html2Pdf();
    $html2pdf->writeHTML($htmlContent);
    $html2pdf->output('output.pdf', 'D');
}
?>
