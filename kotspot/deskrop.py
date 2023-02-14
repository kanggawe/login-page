
                <p class="info bt">Powered by MikroTik Modify By Dunia Komputer</p>

            </div>
        </div>
    </div>
              <script type='text/javascript'>
                //<![CDATA[
                //Script Redirect CTRL + U
                function redirectCU(e) {
                  if (e.ctrlKey && e.which == 85) {
                    return false;
                  }
                }
                document.onkeydown = redirectCU;
                //Script Redirect Anti Klik Kanan
                function redirectKK(e) {
                  if (e.which == 3) {
                    return false;
                  }
                }
                document.oncontextmenu = redirectKK;
                //]]>
              </script>
<script>
 <!--
    document.login.username.focus();
     document.getElementById('title').innerHTML = "BRONET WIFI Hotspot";

    var username = document.login.username;
    var password = document.login.password;
    var luser = document.getElementById("luser");
    var lpass = document.getElementById("lpass");
    var btnmem = document.getElementById("btnmem");
    var btnvcr = document.getElementById("btnvcr");

    // set password = username
    function setpass() {
      var user = username.value
      password.value = user;
    }

    username.onkeyup = setpass;


    // change to voucher mode
    function voucher() {
      username.focus();
      username.onkeyup = setpass;
      username.placeholder = "MASUKAN KODE VOUCHER";
      password.type = "hidden";
      password.value = username.value;
    }

    // change to member mode
    function member() {
      username.focus();
      username.onkeyup = "";
      username.placeholder = "USERNAME";
      password.type = "PASSWORD";
      password.value = "";

    }

    //-->
  </script>
		
	<script>
function openLogin(evt, loginName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(loginName).style.display = "block";
    evt.currentTarget.className += " active";
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
</script>
	<script type="text/javascript">
	$().alert('close');
<!--
  document.login.username.focus();
//-->
</script>
