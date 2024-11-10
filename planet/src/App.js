import Chatbot from "./components/Chatbot";
import Navbar from "./components/Navbar";


// main function where all components are imported from components folder and used
function App() {
  return (
    <>
    {/* component for navbar */}
    <Navbar/>
    {/* component for main chat application */}
    <Chatbot/>
    </>
  );
}

export default App;
