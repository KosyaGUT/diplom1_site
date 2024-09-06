function checkFormreg() {
	const lastName = document.getElementById('last_namereg').value.trim()
	const firstName = document.getElementById('first_namereg').value.trim()
	const patronymic = document.getElementById('patronymicreg').value.trim()
	const birthDate = document.getElementById('birthdatereg').value.trim()
	const email = document.getElementById('emailreg').value.trim()
	const password = document.getElementById('passwordreg').value.trim()
	const confirmPassword = document.getElementById('password2reg').value.trim()
	const agreeTerms = document.getElementById('agreeTermsreg').checked
	const submitButton = document.getElementById('submitButtonreg')

	// Проверка всех условий
	if (
		lastName !== '' &&
		firstName !== '' &&
		patronymic !== '' &&
		birthDate !== '' &&
		email !== '' &&
		password.length >= 6 &&
		password === confirmPassword &&
		agreeTerms
	) {
		submitButton.disabled = false
		submitButton.classList.remove('disabled-button')
		submitButton.classList.add('active-button')
	} else {
		submitButton.disabled = true
		submitButton.classList.remove('active-button')
		submitButton.classList.add('disabled-button')
	}
}

// Применяем функцию на изменение полей ввода и чекбоксов
document.getElementById('last_namereg').addEventListener('input', checkFormreg)
document.getElementById('first_namereg').addEventListener('input', checkFormreg)
document.getElementById('patronymicreg').addEventListener('input', checkFormreg)
document.getElementById('birthdatereg').addEventListener('input', checkFormreg)
document.getElementById('emailreg').addEventListener('input', checkFormreg)
document.getElementById('passwordreg').addEventListener('input', checkFormreg)
document.getElementById('password2reg').addEventListener('input', checkFormreg)
document
	.getElementById('agreeTermsreg')
	.addEventListener('change', checkFormreg) // Используйте "change" для чекбоксов
