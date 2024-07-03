document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const typeInput = document.getElementById('type');
        const categoryInput = document.getElementById('category');
        const amountInput = document.getElementById('amount');
        const descriptionInput = document.getElementById('description');

        if (typeInput.value === '' || categoryInput.value === '' || amountInput.value === '' || descriptionInput.value === '') {
            alert('Form tidak boleh kosong!');
        } else if (isNaN(parseFloat(amountInput.value)) || parseFloat(amountInput.value) <= 0) {
            alert('Jumlah yang dimasukkan harus positif!');
        } else {
            form.submit();
        }
    });
});