function Register() {
    return (
        <div className="bg-[#363654] h-screen w-screen">
            <div className="w-[380px] h-[380px] bg-[#252733] absolute top-[18vh] left-[40vw] rounded-xl">
            <input type="text" placeholder="Email" className="input input-bordered w-full max-w-xs top-4 absolute left-[1.90rem]" />
            <input type="text" placeholder="Username" className="input input-bordered w-full max-w-xs top-[6rem] absolute left-[1.90rem]" />
            <input type="text" placeholder="Password" className="input input-bordered w-full max-w-xs top-[11rem] absolute left-[1.90rem]" />
            <input type="text" placeholder="Confirm Password" className="input input-bordered w-full max-w-xs top-[16rem] absolute left-[1.90rem]" />
            <label htmlFor="my-modal-3" className="btn top-[20rem] absolute left-[8.5rem]">Register</label>
            </div>
        </div>
    )
}

export default Register
