const GET_RECIPES = "recipe/GET_RECIPES"

const getAllRecipes = (recipes) => ({
    type: GET_RECIPES,
    payload: recipes,
})

export const getRecipes = () => async (dispatch) => {
    const response = await fetch("/api/recipes/", {
        headers: {
            "Content-Type": "application/json",
        }
    });
    if (response.ok){
        const data = await response.json();
        if(data.errors){
            return;
        }

        dispatch(getAllRecipes(data))
    }

}


const initialState = {}
export default function reducer(state = initialState, action) {
    const copyState = {...state}
	switch (action.type) {
        case GET_RECIPES:
            let recipes = action.payload.recipes
            recipes.forEach((recipe)=>{
                copyState[recipe.id] = recipe
            })


            return copyState

		default:
			return state;
	}
}
