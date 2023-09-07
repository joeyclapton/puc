public class Main {

    public static void main(String[] args) {
        var developer = new Developer();
        var techLead = new TechLead();
        var manager = new Manager();

        developer.addRoutine("“Programador codifica”");
        developer.addRoutine("“Programador sai para almoçar”");
        developer.addRoutine("“Programador continua condificando”");
        developer.printRoutine();

        techLead.addRoutine("“Líder da equipe distribui tarefas para os programadores”");
        techLead.addRoutine("“Líder da equipe sai para almoçar”");
        techLead.addRoutine("“Líder da equipe auxilia os programadores”");
        techLead.addRoutine("“Líder da equipe encerra o dia de trabalho”");
        techLead.printRoutine();

        manager.addRoutine("“Gerente de projetos reúne com os líderes das equipes”");
        manager.addRoutine("“Gerente de projetos sai para almoçar”");
        manager.addRoutine("“Gerente de projetos analisa novos requisitos”");
        manager.addRoutine("“Gerente de projetos encerra o dia de trabalho”");
        manager.printRoutine();
    }
}
