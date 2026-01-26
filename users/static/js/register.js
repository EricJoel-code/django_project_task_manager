document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.toggle-password').forEach(button => {
        button.addEventListener('click', () => {
            const input = button.closest('label').querySelector('input');
            const icon = button.querySelector('i');

            const show = input.type === 'password';
            input.type = show ? 'text' : 'password';

            icon.classList.toggle('fa-eye', !show);
            icon.classList.toggle('fa-eye-slash', show);
        });
    });
});
