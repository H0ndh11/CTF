import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }
    }

    //セキュリティ監視チームが、安全性の低いドアへの侵入に気づきました。
    //博士の終末計画を守るため 強力なドアを作るよう頼まれました 
    //このドアなら おせっかいな捜査官の侵入を防げるだろう マハッ！
    //
    // -Minion #2671

    //パスワード認証部分
    public boolean checkPassword(String password) {
        //長さは32
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        //0~7文字目はそのままバッファへ
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        //8~15文字目は23-i番目の文字をバッファへ(15,14,...8番目の順)
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        //16,18,20,...30文字目は46-i番目の文字をバッファへ(30,28,...16番目の順)
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        //31,29,27,...17文字目はそのままバッファへ
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm12g94c_u_4_m7ra41");
        //01234567890123456789012345678901
        //0123456789012345-g-4-_-_-_-7-a-1
        //01234567890123454gr4m_4_u_c79a21
        //jU5t_a_s--------4gr4m_4_u_c79a21
        //jU5t_a_s1mpl3_an4gr4m_4_u_c79a21
    }
}
