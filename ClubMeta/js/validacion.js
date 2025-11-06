// --- REGISTRO ---
document.addEventListener("DOMContentLoaded", () => {
  const formRegistro = document.querySelector(".form-registro form");
  const formSesion = document.querySelector(".form-sesion form");

  // Si es la página de REGISTRO
  if (formRegistro) {
    formRegistro.addEventListener("submit", (e) => {
      e.preventDefault();

      // Obtener los datos
      const nombre = document.getElementById("nombre").value;
      const correo = document.getElementById("correo").value;
      const contraseña = document.getElementById("contraseña").value;

      // Guardarlos en localStorage
      localStorage.setItem("nombre", nombre);
      localStorage.setItem("correo", correo);
      localStorage.setItem("contraseña", contraseña);

      alert("✅ Registro exitoso, ahora puedes iniciar sesión.");
      window.location.href = "sesion.html";
    });
  }

  // Si es la página de INICIO DE SESIÓN
  if (formSesion) {
    formSesion.addEventListener("submit", (e) => {
      e.preventDefault();

      const correoIngresado = document.getElementById("email").value;
      const contraseñaIngresada = document.getElementById("contraseña").value;

      const correoGuardado = localStorage.getItem("correo");
      const contraseñaGuardada = localStorage.getItem("contraseña");

      if (correoIngresado === correoGuardado && contraseñaIngresada === contraseñaGuardada) {
        alert("✅ Inicio de sesión exitoso, bienvenido " + localStorage.getItem("nombre") + "!");
        window.location.href = "index.html"; // redirige a la página principal
      } else {
        alert("❌ Correo o contraseña incorrectos.");
      }
    });
  }
});