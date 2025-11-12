// eventos.js
document.addEventListener('DOMContentLoaded', () => {
  // Elementos principales
  const modal = document.getElementById('modal-reserva');
  const closeBtn = modal ? modal.querySelector('.close') : null;
  const confirmarBtn = document.getElementById('confirmar-reserva');
  const nombreEvento = document.getElementById('nombre-evento');
  const fechaInput = document.getElementById('fecha-reserva');

  // Si no existen, salimos sin romper nada
  if (!modal || !closeBtn || !confirmarBtn || !nombreEvento || !fechaInput) {
    console.warn('eventos.js: faltan elementos del DOM (modal/reserva).');
    return;
  }

  // Establecer fecha mínima en el input (hoy)
  (function setMinDateToToday() {
    const today = new Date();
    const yyyy = today.getFullYear();
    const mm = String(today.getMonth() + 1).padStart(2, '0');
    const dd = String(today.getDate()).padStart(2, '0');
    fechaInput.min = `${yyyy}-${mm}-${dd}`;
  })();

  // Abrir modal: delegación para soportar botones creados dinámicamente
  document.body.addEventListener('click', (e) => {
    const btn = e.target.closest('.btn-reservar');
    if (!btn) return;

    const eventoNombre = btn.dataset.evento || 'evento';
    nombreEvento.textContent = eventoNombre;
    fechaInput.value = '';            // limpiar selección previa
    modal.style.display = 'flex';     // mostrar modal (CSS usa flex)
    fechaInput.focus();
  });

  // Cerrar modal - botón
  closeBtn.addEventListener('click', () => {
    modal.style.display = 'none';
  });

  // Cerrar modal - clic fuera del contenido
  window.addEventListener('click', (e) => {
    if (e.target === modal) modal.style.display = 'none';
  });

  // Cerrar con Esc
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.style.display === 'flex') {
      modal.style.display = 'none';
    }
  });

  // Confirmar reserva
  confirmarBtn.addEventListener('click', () => {
    const fecha = fechaInput.value;
    const evento = nombreEvento.textContent || '';

    if (!fecha) {
      alert('Por favor selecciona una fecha.');
      fechaInput.focus();
      return;
    }

    // Aquí puedes enviar la reserva al backend cuando lo implementes.
    // Ejemplo (descomenta y ajusta la URL/estructura cuando tengas API):
    /*
    fetch('/api/reservas', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ evento: evento, fecha: fecha })
    })
    .then(res => res.json())
    .then(data => {
      // manejar respuesta del servidor
      alert('Reserva enviada: ' + data.message);
      modal.style.display = 'none';
    })
    .catch(err => {
      console.error(err);
      alert('Error al enviar la reserva. Intenta más tarde.');
    });
    */

    // Temporal: mostrar confirmación y cerrar modal
    alert(`✅ Reserva solicitada para "${evento}" el ${fecha}.`);
    modal.style.display = 'none';
  });
});
