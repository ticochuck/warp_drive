const $modalLinkEl = $("#link");
const $tableLinksEls = $("#table-body a");

// Add datatables to results table
$(() => {
  $("#result").DataTable({
    searching: true,
    scrollX: true,
    scrollCollapse: false,
    iDisplayLength: 10,
    order: [[0, "desc"]],
  });
});

// Set modal 'Yes' button value to the link of the clicked element
$tableLinksEls.click(function () {
  targetLink = $(this).attr("href");
  $modalLinkEl.attr("href", targetLink);
});


const exampleModal = document.getElementById('exampleModal')
exampleModal.addEventListener('show.modal', (event) => {
  // Button that triggered the modal
  const button = event.relatedTarget
  // Extract info from data-mdb-* attributes
  const recipient = button.getAttribute('data-whatever')
  // If necessary, you could initiate an AJAX request here
  // and then do the updating in a callback.
  //
  // Update the modal's content.
  const modalTitle = exampleModal.querySelector('.modal-title')
  const modalBodyInput = exampleModal.querySelector('.modal-body input')

  modalTitle.textContent = `New message to ${recipient}`
  modalBodyInput.value = recipient
})
