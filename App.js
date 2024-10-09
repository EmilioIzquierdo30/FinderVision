import { useState, useEffect } from "react";
import "./App.css"; // Importa tu archivo CSS
import logoR from './assets/img/logoR.png'; // Importa la imagen del logo

function App() {
    const initialValues = {
        username: "",
        password: "",
    };
    const [formValues, setFormValues] = useState(initialValues);
    const [formErrors, setFormErrors] = useState({});
    const [isSubmit, setIsSubmit] = useState(false);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormValues({ ...formValues, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        setFormErrors(validate(formValues));
        setIsSubmit(true);
    };

    useEffect(() => {
        if (Object.keys(formErrors).length === 0 && isSubmit) {
            console.log(formValues);
        }
    }, [formErrors, formValues, isSubmit]);

    const validate = (values) => {
        const errors = {};
        if (!values.username) {
            errors.username = "Se requiere el usuario!";
        }
        if (!values.password) {
            errors.password = "Se requiere contraseña";
        } else if (values.password.length < 4) {
            errors.password = "La contraseña debe tener más de 4 caracteres";
        } else if (values.password.length > 10) {
            errors.password = "La contraseña no puede exceder más de 10 caracteres";
        }
        return errors;
    };

    return (
        <>
            <div className="bgImg"></div>
            <div className="container">
                <img src={logoR} alt="Logo" className="logo" /> {/* Logo en la parte superior izquierda */}
                {Object.keys(formErrors).length === 0 && isSubmit ? (
                    <div className="ui message success">
                        Registrado exitosamente
                    </div>
                ) : (
                    console.log("Detalles ingresados", formValues)
                )}

                <form onSubmit={handleSubmit}>
                    <h1>Iniciar Sesion</h1>
                    <div className="ui divider"></div>
                    <div className="ui form">
                        <div className="field">
                            <label>Usuario</label>
                            <input
                                type="text"
                                name="username"
                                placeholder="Ingrese su usuario"
                                value={formValues.username}
                                onChange={handleChange}
                            />
                        </div>
                        <p>{formErrors.username}</p>
                        <div className="field">
                            <label>Contraseña</label>
                            <input
                                type="password"
                                name="password"
                                placeholder="Contraseña"
                                value={formValues.password}
                                onChange={handleChange}
                            />
                        </div>
                        <p>{formErrors.password}</p>
                        <button className="fluid ui button blue">Ingresar</button>
                    </div>
                </form>
            </div>
        </>
    );
}

export default App;
