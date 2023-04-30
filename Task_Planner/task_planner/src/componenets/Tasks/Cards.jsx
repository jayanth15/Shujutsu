import "../../App.css"

function Cards(props) {
  return (
    <div className="card card-width bg-[#252733] shadow-xl mt-4 cursor-pointer text-white font-roboto">
      <div className="card-body">
        <h2 className="card-title">Task-Title</h2>
        <p className="truncate">{props.text}</p>
          <div className="card-actions justify-end text-sm">
            <div className="whitespace-pre-wrap">
              Jayz
           </div>
          </div>
          <div className="card-actions justify-end text-sm/[4px]">
            <div>13/10/2023 </div>
          </div>
        </div>
    </div>
  );
}
export default Cards;
