// --- VALIDACIÓN, REGISTRO Y LOGIN ---
document.addEventListener("DOMContentLoaded", () => {
  const formRegistro = document.querySelector(".form-registro form");
  const formSesion = document.querySelector(".form-sesion form");

  //  REGISTRO (solo si existe el formulario y el endpoint /register)
 
  if (formRegistro) {
    formRegistro.addEventListener("submit", async (e) => {
      e.preventDefault();

      const nombre = document.getElementById("nombre").value.trim();
      const telefono = document.getElementById("telefono").value.trim();
      const correo = document.getElementById("correo").value.trim();
      const contrasena = document.getElementById("contraseña").value.trim();

      if (!nombre || !correo || !contrasena) {
        alert("Por favor completa todos los campos.");
        return;
      }

      try {
        const res = await fetch("http://127.0.0.1:5000/registro", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ nombre, telefono, correo, contrasena }),
        });

        const data = await res.json();
        if (res.ok) {
          alert(data.message || "Registro exitoso. Ahora puedes iniciar sesión.");
          window.location.href = "sesion";
        } else {
          alert("X " + (data.message || "Error al registrar."));
        }
      } catch (err) {
        console.error("Error en el registro:", err);
        alert(" Error de conexión con el servidor.");
      }
    });
  }


  if (formSesion) {
    formSesion.addEventListener("submit", async (e) => {
      e.preventDefault();

      const correo = document.getElementById("email").value.trim();
      const contrasena = document.getElementById("contraseña").value.trim();

      if (!correo || !contrasena) {
        alert("Por favor completa todos los campos.");
        return;
      }

      try {
        const res = await fetch("http://127.0.0.1:5000/login", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ correo, contrasena }),
        });

        const data = await res.json();

        if (!res.ok) {
          alert("X " + (data.message || "Correo o contraseña incorrectos."));
          return;
        }
        localStorage.setItem("token", data.access_token);
        localStorage.setItem("rol", data.role);
        localStorage.setItem("correo", correo);

        alert("Bienvenido, inicio de sesión exitoso.");


        if (data.dashboard_url) {
          window.location.href = data.dashboard_url;
        } else {
          window.location.href = "index.html";
        }

      } catch (err) {
        console.error("Error al iniciar sesión:", err);
        alert(" Error de conexión con el servidor.");
      }
    });
  }
});