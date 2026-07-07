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
  
