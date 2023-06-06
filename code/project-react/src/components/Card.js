import Header from "./Header";
import Navigation from "./Navigation";

function Card(){

    return (
        <div className={"container"}>
            <div className={"row"}>
                <div className={"col-12"}>
                    <Header/>
                </div>
            </div>
            <div className={"row"}>
                <div className={"col-12"}>
                    <Navigation/>
                </div>

            </div>
        </div>
    )
}

export default Card