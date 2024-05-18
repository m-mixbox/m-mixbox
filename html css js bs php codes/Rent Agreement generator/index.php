<!doctype html>
<html lang="en">

<head>
  <title>Title</title>
  <!--    meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <!-- Bootstrap CSS v5.2.1 -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
  <link rel="stylesheet" href="styles.css">
  <script src="jquery-3.6.0.js"></script>
  <script src="jquery-3.6.0.min.js"></script>
  <!--<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-validate/1.20.0/jquery.validate.min.js" integrity="sha512-WMEKGZ7L5LWgaPeJtw9MBM4i5w5OSBlSjTjCtSnvFJGSVD26gE5+Td12qN5pvWXhuWaWcVwF++F7aqu9cvqP0A==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>-->
  <!-- ✅ SECOND - load jquery validate ✅ -->
  <script
  src="https://cdnjs.cloudflare.com/ajax/libs/jquery-validate/1.19.3/jquery.validate.min.js"
  integrity="sha512-37T7leoNS06R80c8Ulq7cdCDU5MNQBwlYoy1TX/WUsLFC2eYNqtKlV0QjH7r8JpG/S0GUMZwebnVFLPd6SU5yg=="
  crossorigin="anonymous"
  referrerpolicy="no-referrer">
</script>

<!-- ✅ THIRD - load additional methods ✅ -->
<script
  src="https://cdnjs.cloudflare.com/ajax/libs/jquery-validate/1.19.3/additional-methods.min.js"
  integrity="sha512-XZEy8UQ9rngkxQVugAdOuBRDmJ5N4vCuNXCh8KlniZgDKTvf7zl75QBtaVG1lEhMFe2a2DuA22nZYY+qsI2/xA=="
  crossorigin="anonymous"
  referrerpolicy="no-referrer"
></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/jquery.validation/1.16.0/jquery.validate.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
    jQuery.noConflict();
</script>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.9.3/html2pdf.bundle.min.js" integrity="sha512-YcsIPGdhPK4P/uRW6/sruonlYj+Q7UHWeKfTAkBW+g83NKM+jMJFJ4iAPfSnVp7BKD4dKMHmVSvICUbE/V1sSw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
  <script src="script.js">  </script>
  <!--<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/1.0.272/jspdf.debug.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js" integrity="sha512-BNaRQnYJYiPSqHHDb58B0yaPfCu+Wgds8Gp/gU33kqBtgNS4tSPHuGibyoeqMV/TJlSKda6FXzoEyYGjTe+vXA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>-->
</head>

<body>
  <header>
    <!-- place navbar here -->
  </header>
  <main>
    <!--details form start here-->

    <div class="container">
      <div class="row justify-content-center align-items-center g-2">
        <div class="col-2"></div>
        <div class="col-8">

          <form id="form" action="" >

            <div class="row g-3">
              <div class="col-auto"><label>Enter Place of Execution of Agreement:</label></div>
              <div class="col-auto"><input type="text" class="form-control opacity-75" name="place_of_exec" id="RentF1" placeholder="Eg: Ranchi" required> <br></div>
            </div>
            
            <div class="row g-3">
              <div class="col-auto"><label>Enter Agreement date:</label></div>
              <div class="col-auto"><input type="date" class="form-control  opacity-75" name="agg_date" id="RentF2" placeholder="Eg: 10/9/2023"   required> <br></div>
            </div>


            <div class="row g-3">
              <div class="col-auto"><label>Enter type of 1st Party:</label> <br></div>
              <div class="col-auto"><select required  class="form-select opacity-75 dist1" aria-label="Default select example" id="RentF3" name="party_type_1" > <br>
                <option   selected value="" disabled>not selected</option>
                <option value="individual">individual</option>
                <option value="company">company</option>
              </select><br></div>
            </div>


            <div class="row g-3 ind1">
              <div class="col-auto">
                <label>Enter Name of 1st Party: </label>
              </div>
              <div class="col-auto">
                <select        class="form-select  opacity-75" id="RentF4" name="annotation1" required> 
                  <option   selected value="" disabled>not selected</option>
                  <option value="mr">MR.</option>
                  <option value="mrs">MRS.</option>
                  <option value="mis">MIS.</option>
                  <option value="dr">DR.</option>
                </select>
              </div>
              <div class="col-auto">
                <input type="text" class="form-control  opacity-75" name="name_first_party" id="RentF5" placeholder="Eg: Mrs. Renu" required  > <br>
              </div>
            </div>

            
            <div class="row g-3 comp1">
              <div class="col-auto"><label> CIN of 1st party:</label></div>
              <div class="col-auto"><input type="number" class="form-control  opacity-75" name="cin_1" id="RentF6" placeholder="U86100JH2023PTC020961"   required> <br></div>
            </div>

            <div class="row g-3 comp1">
              <div class="col-auto"><label> Position of person on behalf :</label></div>
              <div class="col-auto"><input type="text" class="form-control  opacity-75" name="behalf_1_pos" id="RentF7" placeholder="Eg: Director"   required> <br></div>
            </div>


            <div class="row g-3 comp1">
              <div class="col-auto"><label> On behalf of 1st party:</label></div>
              <div class="col-auto"><input type="text" class="form-control  opacity-75" name=" behalf_1_name" id="RentF8" placeholder="Eg: Mrs. Renu"   required> <br></div>
            </div>


            <div class="row g-3 comp1">
              <div class="col-auto"><label> DIN of 1st party's representative:</label></div>
              <div class="col-auto"><input type="number" class="form-control  opacity-75" name="din_1" id="RentF9" placeholder="U86100JH2023PTC020961"   required> <br></div>
            </div>


            <div class="row g-3 ind1">
              <div class="col-auto"><label>Enter identification type of 1st party:</label></div>
              <div class="col-auto">
                <select   class="form-select  opacity-75"  required  id="RentF10" name="id_type_1"> 
                  <option   selected value="" disabled>not selected</option>
                  <option value="mr">Aadhar</option>
                  <option value="mrs">Pan card</option>
                  <option value="mis">Driving License</option>
                  <option value="dr">Passport</option>
                </select><br>
              </div>
            </div>
            

            <div class="row g-3 ind1">
              <div class="col-auto"><label>Enter identification no. of 1st party:</label></div>
              <div class="col-auto"><input type="number" class="form-control  opacity-75" name="id_no_1" id="RentF11" placeholder="Eg: 8967 4657 4567"    required> <br></div>
            </div>


            <div class="row g-3">
              <div class="col-auto"><label>Enter residence of 1st party:</label></div>
              <div class="col-auto"><input type="text" class="form-control  opacity-75" name="residence_1" id="RentF12" placeholder="Eg: sonalika tractors,main road,ranchi"  required > <br>
              </div>
            </div>
            

            <div class="row g-3">
              <div class="col-auto"><label>Enter residence pincode of 1st party:</label></div>
              <div class="col-auto"><input type="number" class="form-control  opacity-75" name="pincode_1" id="RentF13" placeholder="Eg: 346758"  required > <br></div>
            </div>


            <div class="row g-3">
              <div class="col-auto"><label>Enter type of 2nd Party:</label> <br></div>
              <div class="col-auto"><select     class="form-select opacity-75 dist2" aria-label="Default select example" id="RentF14" name="dropdown1" required> <br>
                <option   selected value="" disabled >not selected</option>
                <option value="individual">individual</option>
                <option value="company">company</option>
              </select><br></div>
            </div>
            

            <div class="row g-3 ind2">
              <div class="col-auto">
                <label>Enter Name of 2nd Party: </label>
              </div>
              <div class="col-auto">
                <select     required   class="form-select  opacity-75 " id="RentF15" name="dropdown3"> 
                  <option   selected value="" disabled>not selected</option>
                  <option value="mr">MR.</option>
                  <option value="mrs">MRS.</option>
                  <option value="mis">MIS.</option>
                  <option value="dr">DR.</option>
                </select>
              </div>
              <div class="col-auto">
                <input type="text" class="form-control  opacity-75" name="name_first" id="RentF16" placeholder="Eg: Mrs. Renu"   required> <br>
              </div>
            </div>
            

            <div class="row g-3 comp2">
              <div class="col-auto"><label> CIN of 2nd party:</label></div>
              <div class="col-auto"><input type="number" class="form-control  opacity-75 comp2" name=" " id="RentF17" placeholder="U86100JH2023PTC020961"   required> <br></div>
            </div>

            <div class="row g-3 comp2">
              <div class="col-auto"><label> Position of person on behalf :</label></div>
              <div class="col-auto"><input type="text" class="form-control  opacity-75 " name=" " id="RentF18" placeholder="Eg: Director"   required> <br></div>
            </div>


            <div class="row g-3 comp2">
              <div class="col-auto"><label>On behalf of 2nd party:</label></div>
              <div class="col-auto"><input type="text" class="form-control  opacity-75 comp2" name=" " id="RentF19" placeholder="Eg: Mrs. Renu"   required> <br></div>
            </div>
            

            <div class="row g-3 comp2">
              <div class="col-auto"><label> DIN of 2nd party's representative:</label></div>
              <div class="col-auto"><input type="number" class="form-control  opacity-75 " name=" " id="RentF20" placeholder="U86100JH2023PTC020961"   required> <br></div>
            </div>
            
            <div class="row g-3 ind2">
              <div class="col-auto"><label>Enter identification type of 2nd party:</label></div>
              <div class="col-auto">
                <select    class="form-select  opacity-75 "   id="RentF21" required> 
                  <option   selected value="">not selected</option>
                  <option value="mr">Aadhar</option>
                  <option value="mrs">Pan card</option>
                  <option value="mis">Driving License</option>
                  <option value="dr">Passport</option>
                </select><br>
              </div>
            </div>
            
            <div class="row g-3 ind2">
              <div class="col-auto"><label>Enter identification no. of 2nd party:</label></div>
              <div class="col-auto"><input type="number" class="form-control  opacity-75 " name=" " id="RentF22" placeholder="Eg: 8967 4657 4567"   required> <br></div>
            </div>


            <div class="row g-3">
              <div class="col-auto"><label>Enter residence of 2nd party:</label></div>
              <div class="col-auto"><input type="text" class="form-control  opacity-75" name=" " id="RentF23" placeholder="Eg: sonalika tractors,main road,ranchi" required  > <br></div>
            </div>

            <div class="row g-3">
              <div class="col-auto"><label>Enter residence pincode of 2nd party:</label></div>
              <div class="col-auto"><input type="number" class="form-control  opacity-75" name=" " id="RentF24" placeholder="Eg: 657890"  required > <br></div>
            </div>


            <div class="row g-3">
              <div class="col-auto"><label>Enter location of property:</label></div>
              <div class="col-auto"><input type="text" class="form-control  opacity-75" name=" " id="RentF25" placeholder="Eg: Mrs. Renu"   required> <br>
              </div>
            </div>
            
            <div class="row g-3">
              <div class="col-auto"><label>Enter pincode  of property:</label></div>
              <div class="col-auto"><input type="number" class="form-control  opacity-75" name=" " id="RentF26" placeholder="Eg: Ranchi"  required > <br></div>
            </div>
            
            <div class="row g-3">
              <div class="col-auto"><label>Enter Agreement starting date:</label></div>
              <div class="col-auto"><input type="number" class="form-control  opacity-75" name=" " id="RentF27" placeholder="Eg: 10"   required> <br></div>
            </div>
            
            <div class="row g-3">
              <div class="col-auto"><label>Enter Agreement tenure:</label></div>
              <div class="col-auto"><input type="number" class="form-control  opacity-75" name=" " id="RentF28" placeholder="Eg: 6"  required > <br>
              </div>
            </div>
            
            <div class="row g-3">
              <div class="col-auto"><label>Enter rent per month:</label></div>
              <div class="col-auto"><input type="number" class="form-control  opacity-75" name=" " id="RentF29" placeholder="Eg: 5000"   required> <br></div>
            </div>
            
            <div class="row g-3">
              <div class="col-auto"><label>Enter rent payment date:</label></div>
              <div class="col-auto"><input type="number" class="form-control  opacity-75" name=" " id="RentF30" placeholder="Eg: 1"  required > <br></div>
            </div>
            
            <!--<div class="row g-3">
              <div class="col-auto"><label>Enter Agreement commencement date:</label></div>
              <div class="col-auto"><input type="date" class="form-control  opacity-75" name=" " id="RentF31" placeholder="Eg: 10/9/2023"   required> <br></div>
            </div>-->


            <div class="row g-3">
              <div class="col-auto"><label>Enter Agreement commencement date:</label></div>
              <div class="col-auto"><input type="date" class="form-control  opacity-75" name=" " id="RentF32" placeholder="Eg: 10/9/2023"   required> <br></div>
            </div>
            
            <div class="row g-3">
              <div class="col-auto"><label>Witness</label><br></div>
              <div class="col-auto"><input type="text" class="form-control  opacity-75" name=" " id="RentF33" placeholder="Eg: enter the name of witness"   required> <br></div>
            </div>
            

            <button id="add_witness" class="btn btn-primary mb-2" type="button" >add witness</button><br>

            
            <input type="submit" class="btn btn-primary" id="RentFSubmit" value="submit" ><br>
          </form>



        </div>
        <div class="col-2"></div>
      </div>
    </div>

    <!--content of aggrement starts here -->
    <div class="container "><button class="btn btn-primary" id="edit">edit</button></div>
    <div class="container " id="hidden" style="text-align: justify;text-justify: inter-word;">
      
      <div class="row justify-content-center align-items-center g-2">
        
      <h2 class="text-center">RENT AGREEMENT</h2>
      <div>
        This Rent Agreement is executed at <span>Ranchi</span> on this <span>Saturday</span>,<span>18th of December 2023</span><br>
        <div class="text-center">
           BETWEEN
        </div>
        
      </div>
      <div>
        <span>Shri Binod Kumar Agarwal</span> having <span>Aadhar no. 316521991223</span> resident at <span>704/JS/A , Sri Sai Kunj , RRB Colony, Hanuman Mandir Lane , Opposite Laxmi Apartment , Hehal , Ranchi </span> - <span>834004</span> . (Hereinafter reffered to as 'OWNER' which expression shall mean and include its hiers , succesors and assigns ) of the FIRST PART. <br>

        <div class="text-center">AND</div>

      </div>
      <div>
        <span type="name" placeholder="name of 2nd party"   id="value5">Medifirst Hospitals Private Limited</span> having <span>CIN: U86100JH2023PTC020961</span> through its<span> Director Dr. Ankur Saurav (DIN: 10261323) </span>resident at<span id="value6" type="name" placeholder="residence"  > S/O S. S. Lal, 205A Shree Sai Aashray Apartment, Argora, Kathal More Road, Pundag, Ratu, Ranchi, Jharkhand</span> - <span id="value7" type="name" placeholder="pincode"  >834004</span>.(Hereinafter referred to as the “TENANT” which expression shall mean and include its assigns, successors in title) of the SECOND PART.

      </div></br>
      <div> 
        WHEREAS the OWNER is the original owner of the property situated at <span id="value8" type="name" placeholder="location of property"  >704/J2/A, Sri Sai Kunj, R R B Colony, Hanuman Mandir Lane, Opposite Laxmi Apartment, Hehal, Ranchi, Jharkhand</span> - <span id="value9" type="name" placeholder="pincode"  >834005</span> has agreed to rent out the said premises             On a monthly rental basis for a period of <span id="value10" type="name" placeholder="tenure duration"  >11 (eleven)</span> months only             On terms and conditions hereinafter set forth.
WHEREAS the TENANT has approached to the OWNER to let out the above said property for opening registered office of his business and that OWNER is in position to let out the aforesaid property for renting and TENANT is agreeable to accept the same for the registered office of his business. <br>
        <div class="text-center">AND</div> 
<div>The TENANT and OWNER has agreed to give             On rent the above-mentioned premises             On terms and conditions set out hereunder.</div>

      </div></br>
      <div id="terms"> <br>
        NOW THIS RENT AGREEMENT WITNESSETH AS UNDER
        <ol>
          <li>The rental agreement will commence effective from <span placeholder="date"   id="value11">19-08-2023</span>. The rent is for the period of <span type="name"   placeholder="tenure of aggrement" id="value12">11</span> months</li>
          <li>The tenant shall pay the owner             On every month a consolidated sum of Rs  <span placeholder="rent amount"   id="value13">5,000 </span> <span placeholder="rent amount in words"   id="value14">(Rupees Five Thousand only)</span> as maintenance as per actual demand. The rent shall be paid             On or before the <span placeholder=" date of rent amount payment"   id="value15">10th</span> of the succeeding month.
          </li>
          <li>The tenant shall pay the electricity charges in respect of the rented property during the period of rental agreement before the due dates.
          </li>
          <li id="page_break_after">The tenant shall be entitled to fix temporary fittings, fixtures and appliances in the rented property with the consent of the owner and shall be liberty to remove them while vacating thee rented property without causing damage to the construction and walls</li>
          <li class="page_break_before">The tenant shall not make any structural additions or alteration to the rented property</li>
          <li >            On termination of this rental agreement the TENANT shall hand over vacant possession of the rented property along with the permanent fixtures listed to the OWNER in good condition only</li>
          <li >The tenant shall replace at their cost of all the fittings, electrical installment, etc., damaged by the tenant and all expenses for the maintenance of these items shall be borne by the tenant</li>
          <li>The owner shall pay the urban tax, municipal taxes and other taxes and outgoing both present and future in respect of the rented property up to date and ensure uninterrupted occupation by the tenant during the period of rental agreement</li>
          <li ><div>In the event of the tenant vacating the rented space he should give three months' notice in writing for the termination of the agreement during the currency of the agreement.</div>
          </li>
          <li >In the event of such earlier termination, the tenant shall pay the common maintenances and the block maintenance respectively.
          </li>
          <span id="warning"></span>
          <button class="btn btn-primary" id="add_condition">add condition</button>
        </ol>
      </div></br>
      <div>In WITNESS WHERE OF the OWNER and the TENANT have hereunto subscribed their hand             On this <span placeholder="date of aggrement"   id="value16">19th day of AUGUST, 2023</span> in the presence of the following Witnesses.
      </div></br>

      <div class="row justify-content-end mt-3">
        <div class="col-6  align-self-center">
          <div class="text-center">FOR, <span type="name"   placeholder="company name">MEDIFIRST HOSPITALS PVT. LTD.</span><br></div>
        </div>
      </div>
      <div class="row mt-5">
        <p>&nbsp;</p>
        <div class="col-6 text-center align-self-end">
          <span id="">SHRI. BINOD KUMAR AGRAWAL</span> <br>
                   OWNER
        </div>
        <div class="col-6 text-center align-self-end">
          
            
            <div></div>
            <span>DR. ANKUR SAURAV</span> <br>
                   TENANT</br>
          
        </div>

      </div>
      
      <div>
        Witness <ol type="number">
                   <li><span>ab</span></li>
                   <li><span>bd</span></li>
                   <li><span>ch</span></li>
                </ol>
      </div>
      </div>
    </div>
    <div class="container">
      <button class="btn btn-primary" id="print">print</button>
    </div>
    </div>
  </main>
  <footer>
    <!-- place footer here -->
  </footer>
  <!-- Bootstrap JavaScript Libraries -->
<script>
 
 
</script>
  
  <script
			  src="https://code.jquery.com/jquery-3.7.1.min.js"
			  integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo="
			  crossorigin="anonymous"></script>

  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"
    integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous">
  </script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js"
    integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous">
  </script>
</body>

</html>