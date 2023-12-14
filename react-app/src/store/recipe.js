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



export default function reducer(state = {}, action) {
	switch (action.type) {
        case GET_RECIPES:
            return {recipes: action.payload}

		default:
			return state;
	}
}
