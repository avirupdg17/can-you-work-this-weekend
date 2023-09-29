import GetStarted from "./components/Dashboard/GetStarted/GetStarted";
import Background from "./pages/Background/Background";
import Header from "./pages/Header/Header";

export default function App() {
  return (
    <div className="bg-white">
      <Header />
      <Background>
        <GetStarted />
      </Background>
    </div>
  );
}
