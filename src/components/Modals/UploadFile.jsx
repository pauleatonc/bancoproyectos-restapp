import ModalBase  from './ModalBase';

const UploadFile = () =>
{
  return (
    <>
      <ModalBase title="Agregar archivo adicional" btnName="Subir Archivo" btnIcon="add" modalID="uploadFile">
        <div className="d-flex align-items-center" >
          <div className=" col-12 d-flex border-top justify-content-between">
            <button className="btn-borderless d-flex justify-content-between my-5" data-bs-dismiss="modal" aria-label="Close">
              <i className="material-symbols-rounded ms-2 fs-2 mt-1">keyboard_arrow_left</i>
              <p className="text-sans-p-blue text-decoration-underline mb-0 py-1 px-2">Volver a la solicitud</p>
            </button>
            <button
              className="btn-principal-s d-flex text-sans-h4 pb-0 me-3 align-self-center"
            >
              <p className="text-sans-p-white text-decoration-underline">Guardar</p>
              <i className="material-symbols-rounded ms-2 pt-1">save</i>
            </button>
          </div>
        </div>
      </ModalBase>
    </>

  )
}

export default UploadFile; 