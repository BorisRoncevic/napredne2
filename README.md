* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Arial, sans-serif;
}

.login-frame {
  min-height: 100vh;
  width: 100%;

  display: flex;
  align-items: center;
  justify-content: center;

  padding-top: 64px;
  padding-bottom: 64px;

  background-color: rgba(37, 37, 37, 0.3);
  backdrop-filter: blur(8px);

  /* Ako imaš background sliku, ubaci je ovde */
  background-image:
    linear-gradient(rgba(37, 37, 37, 0.3), rgba(37, 37, 37, 0.3)),
    url("/parking-bg.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.login-modal {
  width: 600px;
  min-height: 529px;

  display: flex;
  flex-direction: column;
  gap: 80px;

  padding: 16px 32px 32px 32px;

  background-color: rgba(37, 37, 37, 0.85);
  border: 2px solid #ffffff;
  border-radius: 16px;

  box-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);

  color: #ffffff;
}

.login-modal-header {
  width: 100%;
  height: 40px;

  display: flex;
  align-items: center;
  justify-content: space-between;
}

.login-modal-header h1 {
  margin: 0;
  font-size: 32px;
  font-weight: 700;
  color: #ffffff;
}

.login-modal-body {
  width: 100%;

  display: flex;
  flex-direction: column;
  gap: 16px;
}

.form-field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.form-field label {
  font-size: 14px;
  font-weight: 600;
  color: #ffffff;
}

.form-field input {
  width: 100%;
  height: 48px;

  border: 2px solid #ffffff;
  border-radius: 8px;

  background-color: transparent;
  color: #ffffff;

  padding: 0 14px;

  font-size: 16px;
  outline: none;
}

.form-field input:focus {
  border-color: #7effc6;
}

.password-input-wrapper {
  position: relative;
  width: 100%;
}

.password-input-wrapper input {
  padding-right: 48px;
}

.password-toggle {
  position: absolute;
  top: 50%;
  right: 12px;

  transform: translateY(-50%);

  width: 32px;
  height: 32px;

  border: none;
  background: transparent;

  color: #ffffff;
  cursor: pointer;
}

.login-modal-footer {
  width: 288px;
  height: 35px;

  display: flex;
  flex-direction: column;
  gap: 8px;

  align-self: center;
}

.login-button {
  width: 288px;
  height: 35px;
  max-width: 288px;

  display: flex;
  align-items: center;
  justify-content: center;

  padding: 8px 64px;

  border: none;
  border-radius: 24px;

  background-color: #7effc6;
  color: #252525;

  font-size: 14px;
  font-weight: 600;

  cursor: pointer;
}

.login-button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.login-error {
  margin: -50px 0 0 0;
  color: #ff8a8a;
  font-size: 14px;
  text-align: center;
}
