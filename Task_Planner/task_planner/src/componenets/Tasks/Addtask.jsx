import MyListbox from "./Listbox";

function Modal() {
    let list = ["first-task", "second-task", "first-task", "second-task"]
  return (
    <div className="relative w-full">
      <label htmlFor="my-modal-3" className="rounded-full btn btn-circle bg-[#6D5DD3]
          flex items-center justify-center hover:rounded-lg hover:bg-[#d3ccff]
          text-white text-2xl m-2 absolute w-18 top-2 right-4">
        +
      </label>
      <input type="checkbox" id="my-modal-3" className="modal-toggle" />
      <div className="modal">
        <div className="modal-box relative  bg-blue-500">
          <label
            htmlFor="my-modal-3"
            className="btn btn-sm btn-circle absolute right-2 top-2"
          >
            ✕
          </label>
          <input type="text" placeholder="Title" className="input input-bordered w-full max-w-xs" />
          <textarea className="textarea textarea-bordered mt-4 w-4/5" placeholder="Descrption"></textarea>
          <div className="relative w-full">
          <MyListbox />
          </div>
          <input type="text" placeholder="add task" className="input input-bordered w-full max-w-xs mt-12" />
          <div htmlFor="my-modal-3" className="btn btn-circle ml-2 mt-2"> + </div>
          <div className="mt-2">
            {list.map(task => (
                <div>
                <li>{task} <div className=" ml-8 btn btn-sm w-6 h-[1px]">-</div></li>
                </div>
            ))}
          </div>
          <div className="modal-action">
           <label htmlFor="my-modal-3" className="btn">Create Task</label>
            </div>
        </div>
      </div>
    </div>
  );
}

export default Modal
