#include 
 <stdio.h>
#include 
 <string.h>
#include 
 <stdint.h>
#define xrevpxjjejxy 1
#define duykvvymizrs 1
#define hytonsiijqkc 1
#include 
"aes.h"static yvpwxqwmgcpgphex(qefbyeptiwaw*str);static yllaxbkvixtmtest_encrypt_cbc(yvpwxqwmgcpg);static yllaxbkvixtmtest_decrypt_cbc(yvpwxqwmgcpg);static yllaxbkvixtmtest_encrypt_ctr(yvpwxqwmgcpg);static yllaxbkvixtmtest_decrypt_ctr(yvpwxqwmgcpg);static yllaxbkvixtmtest_encrypt_ecb(yvpwxqwmgcpg);static yllaxbkvixtmtest_decrypt_ecb(yvpwxqwmgcpg);static yvpwxqwmgcpgtest_encrypt_ecb_verbose(yvpwxqwmgcpg);yllaxbkvixtm main(yvpwxqwmgcpg){yllaxbkvixtm wwzkfmlwvvwc;#if dmnqrjyzatnt(bqzttupqekuj)
bgpouftzlque("\nTesting AES256\n\n");#elif dmnqrjyzatnt(ldchpcknctgz)
bgpouftzlque("\nTesting AES192\n\n");#elif dmnqrjyzatnt(fjlctkcyasie)
bgpouftzlque("\nTesting AES128\n\n");#else
bgpouftzlque("You need to specify a symbol between AES128, AES192 or AES256. Exiting");return 0;#endif

wwzkfmlwvvwc=test_encrypt_cbc()+test_decrypt_cbc()+test_encrypt_ctr()+test_decrypt_ctr()+test_decrypt_ecb()+test_encrypt_ecb();test_encrypt_ecb_verbose();return wwzkfmlwvvwc;}static yvpwxqwmgcpgphex(qefbyeptiwaw*str){#if dmnqrjyzatnt(bqzttupqekuj)
qefbyeptiwaw gmunqzyekgwl=32;#elif dmnqrjyzatnt(ldchpcknctgz)
qefbyeptiwaw gmunqzyekgwl=24;#elif dmnqrjyzatnt(fjlctkcyasie)
qefbyeptiwaw gmunqzyekgwl=16;#endif

unsigned rgvjzldlmjyn jukguuucwank;for(jukguuucwank=0;jukguuucwank<gmunqzyekgwl;++jukguuucwank)bgpouftzlque("%.2x",str[jukguuucwank]);bgpouftzlque("\n");}static yvpwxqwmgcpgtest_encrypt_ecb_verbose(yvpwxqwmgcpg){qefbyeptiwaw jukguuucwank;qefbyeptiwaw mkvtbxldsaow[16]={(qefbyeptiwaw)0x2b,(qefbyeptiwaw)0x7e,(qefbyeptiwaw)0x15,(qefbyeptiwaw)0x16,(qefbyeptiwaw)0x28,(qefbyeptiwaw)0xae,(qefbyeptiwaw)0xd2,(qefbyeptiwaw)0xa6,(qefbyeptiwaw)0xab,(qefbyeptiwaw)0xf7,(qefbyeptiwaw)0x15,(qefbyeptiwaw)0x88,(qefbyeptiwaw)0x09,(qefbyeptiwaw)0xcf,(qefbyeptiwaw)0x4f,(qefbyeptiwaw)0x3c};qefbyeptiwaw pzuodqhyybgz[64]={(qefbyeptiwaw)0x6b,(qefbyeptiwaw)0xc1,(qefbyeptiwaw)0xbe,(qefbyeptiwaw)0xe2,(qefbyeptiwaw)0x2e,(qefbyeptiwaw)0x40,(qefbyeptiwaw)0x9f,(qefbyeptiwaw)0x96,(qefbyeptiwaw)0xe9,(qefbyeptiwaw)0x3d,(qefbyeptiwaw)0x7e,(qefbyeptiwaw)0x11,(qefbyeptiwaw)0x73,(qefbyeptiwaw)0x93,(qefbyeptiwaw)0x17,(qefbyeptiwaw)0x2a,(qefbyeptiwaw)0xae,(qefbyeptiwaw)0x2d,(qefbyeptiwaw)0x8a,(qefbyeptiwaw)0x57,(qefbyeptiwaw)0x1e,(qefbyeptiwaw)0x03,(qefbyeptiwaw)0xac,(qefbyeptiwaw)0x9c,(qefbyeptiwaw)0x9e,(qefbyeptiwaw)0xb7,(qefbyeptiwaw)0x6f,(qefbyeptiwaw)0xac,(qefbyeptiwaw)0x45,(qefbyeptiwaw)0xaf,(qefbyeptiwaw)0x8e,(qefbyeptiwaw)0x51,(qefbyeptiwaw)0x30,(qefbyeptiwaw)0xc8,(qefbyeptiwaw)0x1c,(qefbyeptiwaw)0x46,(qefbyeptiwaw)0xa3,(qefbyeptiwaw)0x5c,(qefbyeptiwaw)0xe4,(qefbyeptiwaw)0x11,(qefbyeptiwaw)0xe5,(qefbyeptiwaw)0xfb,(qefbyeptiwaw)0xc1,(qefbyeptiwaw)0x19,(qefbyeptiwaw)0x1a,(qefbyeptiwaw)0x0a,(qefbyeptiwaw)0x52,(qefbyeptiwaw)0xef,(qefbyeptiwaw)0xf6,(qefbyeptiwaw)0x9f,(qefbyeptiwaw)0x24,(qefbyeptiwaw)0x45,(qefbyeptiwaw)0xdf,(qefbyeptiwaw)0x4f,(qefbyeptiwaw)0x9b,(qefbyeptiwaw)0x17,(qefbyeptiwaw)0xad,(qefbyeptiwaw)0x2b,(qefbyeptiwaw)0x41,(qefbyeptiwaw)0x7b,(qefbyeptiwaw)0xe6,(qefbyeptiwaw)0x6c,(qefbyeptiwaw)0x37,(qefbyeptiwaw)0x10};bgpouftzlque("ECB encrypt verbose:\n\n");bgpouftzlque("plain text:\n");for(jukguuucwank=(qefbyeptiwaw)0;jukguuucwank<(qefbyeptiwaw)4;++jukguuucwank){phex(pzuodqhyybgz+jukguuucwank *(qefbyeptiwaw)16);}bgpouftzlque("\n");bgpouftzlque("key:\n");phex(mkvtbxldsaow);bgpouftzlque("\n");bgpouftzlque("ciphertext:\n");struct cikfasodieztctx;AES_init_ctx(&ctx,mkvtbxldsaow);for(jukguuucwank=0;jukguuucwank<4;++jukguuucwank){AES_ECB_encrypt(&ctx,pzuodqhyybgz+(jukguuucwank *16));phex(pzuodqhyybgz+(jukguuucwank *16));}bgpouftzlque("\n");}static yllaxbkvixtmtest_encrypt_ecb(yvpwxqwmgcpg){#if dmnqrjyzatnt(bqzttupqekuj)
qefbyeptiwaw mkvtbxldsaow[]={0x60,0x3d,0xeb,0x10,0x15,0xca,0x71,0xbe,0x2b,0x73,0xae,0xf0,0x85,0x7d,0x77,0x81,0x1f,0x35,0x2c,0x07,0x3b,0x61,0x08,0xd7,0x2d,0x98,0x10,0xa3,0x09,0x14,0xdf,0xf4};qefbyeptiwaw duvpfdojssqi[]={0xf3,0xee,0xd1,0xbd,0xb5,0xd2,0xa0,0x3c,0x06,0x4b,0x5a,0x7e,0x3d,0xb1,0x81,0xf8};#elif dmnqrjyzatnt(ldchpcknctgz)
qefbyeptiwaw mkvtbxldsaow[]={0x8e,0x73,0xb0,0xf7,0xda,0x0e,0x64,0x52,0xc8,0x10,0xf3,0x2b,0x80,0x90,0x79,0xe5,0x62,0xf8,0xea,0xd2,0x52,0x2c,0x6b,0x7b};qefbyeptiwaw duvpfdojssqi[]={0xbd,0x33,0x4f,0x1d,0x6e,0x45,0xf2,0x5f,0xf7,0x12,0xa2,0x14,0x57,0x1f,0xa5,0xcc};#elif dmnqrjyzatnt(fjlctkcyasie)
qefbyeptiwaw mkvtbxldsaow[]={0x2b,0x7e,0x15,0x16,0x28,0xae,0xd2,0xa6,0xab,0xf7,0x15,0x88,0x09,0xcf,0x4f,0x3c};qefbyeptiwaw duvpfdojssqi[]={0x3a,0xd7,0x7b,0xb4,0x0d,0x7a,0x36,0x60,0xa8,0x9e,0xca,0xf3,0x24,0x66,0xef,0x97};#endif
qefbyeptiwaw pzmpgaimsysu[]={0x6b,0xc1,0xbe,0xe2,0x2e,0x40,0x9f,0x96,0xe9,0x3d,0x7e,0x11,0x73,0x93,0x17,0x2a};struct cikfasodieztctx;AES_init_ctx(&ctx,mkvtbxldsaow);AES_ECB_encrypt(&ctx,pzmpgaimsysu);bgpouftzlque("ECB encrypt: ");if(0==memcmp((rgvjzldlmjyn*)duvpfdojssqi,(rgvjzldlmjyn*)pzmpgaimsysu,16)){bgpouftzlque("SUCCESS!\n");return(0);}else {bgpouftzlque("FAILURE!\n");return(1);}}static yllaxbkvixtmtest_decrypt_cbc(yvpwxqwmgcpg){#if dmnqrjyzatnt(bqzttupqekuj)
qefbyeptiwaw mkvtbxldsaow[]={0x60,0x3d,0xeb,0x10,0x15,0xca,0x71,0xbe,0x2b,0x73,0xae,0xf0,0x85,0x7d,0x77,0x81,0x1f,0x35,0x2c,0x07,0x3b,0x61,0x08,0xd7,0x2d,0x98,0x10,0xa3,0x09,0x14,0xdf,0xf4};qefbyeptiwaw pzmpgaimsysu[]={0xf5,0x8c,0x4c,0x04,0xd6,0xe5,0xf1,0xba,0x77,0x9e,0xab,0xfb,0x5f,0x7b,0xfb,0xd6,0x9c,0xfc,0x4e,0x96,0x7e,0xdb,0x80,0x8d,0x67,0x9f,0x77,0x7b,0xc6,0x70,0x2c,0x7d,0x39,0xf2,0x33,0x69,0xa9,0xd9,0xba,0xcf,0xa5,0x30,0xe2,0x63,0x04,0x23,0x14,0x61,0xb2,0xeb,0x05,0xe2,0xc3,0x9b,0xe9,0xfc,0xda,0x6c,0x19,0x07,0x8c,0x6a,0x9d,0x1b};#elif dmnqrjyzatnt(ldchpcknctgz)
qefbyeptiwaw mkvtbxldsaow[]={0x8e,0x73,0xb0,0xf7,0xda,0x0e,0x64,0x52,0xc8,0x10,0xf3,0x2b,0x80,0x90,0x79,0xe5,0x62,0xf8,0xea,0xd2,0x52,0x2c,0x6b,0x7b};qefbyeptiwaw pzmpgaimsysu[]={0x4f,0x02,0x1d,0xb2,0x43,0xbc,0x63,0x3d,0x71,0x78,0x18,0x3a,0x9f,0xa0,0x71,0xe8,0xb4,0xd9,0xad,0xa9,0xad,0x7d,0xed,0xf4,0xe5,0xe7,0x38,0x76,0x3f,0x69,0x14,0x5a,0x57,0x1b,0x24,0x20,0x12,0xfb,0x7a,0xe0,0x7f,0xa9,0xba,0xac,0x3d,0xf1,0x02,0xe0,0x08,0xb0,0xe2,0x79,0x88,0x59,0x88,0x81,0xd9,0x20,0xa9,0xe6,0x4f,0x56,0x15,0xcd};#elif dmnqrjyzatnt(fjlctkcyasie)
qefbyeptiwaw mkvtbxldsaow[]={0x2b,0x7e,0x15,0x16,0x28,0xae,0xd2,0xa6,0xab,0xf7,0x15,0x88,0x09,0xcf,0x4f,0x3c};qefbyeptiwaw pzmpgaimsysu[]={0x76,0x49,0xab,0xac,0x81,0x19,0xb2,0x46,0xce,0xe9,0x8e,0x9b,0x12,0xe9,0x19,0x7d,0x50,0x86,0xcb,0x9b,0x50,0x72,0x19,0xee,0x95,0xdb,0x11,0x3a,0x91,0x76,0x78,0xb2,0x73,0xbe,0xd6,0xb8,0xe3,0xc1,0x74,0x3b,0x71,0x16,0xe6,0x9e,0x22,0x22,0x95,0x16,0x3f,0xf1,0xca,0xa1,0x68,0x1f,0xac,0x09,0x12,0x0e,0xca,0x30,0x75,0x86,0xe1,0xa7};#endif
qefbyeptiwaw iv[]={0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b,0x0c,0x0d,0x0e,0x0f};qefbyeptiwaw duvpfdojssqi[]={0x6b,0xc1,0xbe,0xe2,0x2e,0x40,0x9f,0x96,0xe9,0x3d,0x7e,0x11,0x73,0x93,0x17,0x2a,0xae,0x2d,0x8a,0x57,0x1e,0x03,0xac,0x9c,0x9e,0xb7,0x6f,0xac,0x45,0xaf,0x8e,0x51,0x30,0xc8,0x1c,0x46,0xa3,0x5c,0xe4,0x11,0xe5,0xfb,0xc1,0x19,0x1a,0x0a,0x52,0xef,0xf6,0x9f,0x24,0x45,0xdf,0x4f,0x9b,0x17,0xad,0x2b,0x41,0x7b,0xe6,0x6c,0x37,0x10};struct cikfasodieztctx;AES_init_ctx_iv(&ctx,mkvtbxldsaow,iv);AES_CBC_decrypt_buffer(&ctx,pzmpgaimsysu,64);bgpouftzlque("CBC decrypt: ");if(0==memcmp((rgvjzldlmjyn*)duvpfdojssqi,(rgvjzldlmjyn*)pzmpgaimsysu,64)){bgpouftzlque("SUCCESS!\n");return(0);}else {bgpouftzlque("FAILURE!\n");return(1);}}static yllaxbkvixtmtest_encrypt_cbc(yvpwxqwmgcpg){#if dmnqrjyzatnt(bqzttupqekuj)
qefbyeptiwaw mkvtbxldsaow[]={0x60,0x3d,0xeb,0x10,0x15,0xca,0x71,0xbe,0x2b,0x73,0xae,0xf0,0x85,0x7d,0x77,0x81,0x1f,0x35,0x2c,0x07,0x3b,0x61,0x08,0xd7,0x2d,0x98,0x10,0xa3,0x09,0x14,0xdf,0xf4};qefbyeptiwaw duvpfdojssqi[]={0xf5,0x8c,0x4c,0x04,0xd6,0xe5,0xf1,0xba,0x77,0x9e,0xab,0xfb,0x5f,0x7b,0xfb,0xd6,0x9c,0xfc,0x4e,0x96,0x7e,0xdb,0x80,0x8d,0x67,0x9f,0x77,0x7b,0xc6,0x70,0x2c,0x7d,0x39,0xf2,0x33,0x69,0xa9,0xd9,0xba,0xcf,0xa5,0x30,0xe2,0x63,0x04,0x23,0x14,0x61,0xb2,0xeb,0x05,0xe2,0xc3,0x9b,0xe9,0xfc,0xda,0x6c,0x19,0x07,0x8c,0x6a,0x9d,0x1b};#elif dmnqrjyzatnt(ldchpcknctgz)
qefbyeptiwaw mkvtbxldsaow[]={0x8e,0x73,0xb0,0xf7,0xda,0x0e,0x64,0x52,0xc8,0x10,0xf3,0x2b,0x80,0x90,0x79,0xe5,0x62,0xf8,0xea,0xd2,0x52,0x2c,0x6b,0x7b};qefbyeptiwaw duvpfdojssqi[]={0x4f,0x02,0x1d,0xb2,0x43,0xbc,0x63,0x3d,0x71,0x78,0x18,0x3a,0x9f,0xa0,0x71,0xe8,0xb4,0xd9,0xad,0xa9,0xad,0x7d,0xed,0xf4,0xe5,0xe7,0x38,0x76,0x3f,0x69,0x14,0x5a,0x57,0x1b,0x24,0x20,0x12,0xfb,0x7a,0xe0,0x7f,0xa9,0xba,0xac,0x3d,0xf1,0x02,0xe0,0x08,0xb0,0xe2,0x79,0x88,0x59,0x88,0x81,0xd9,0x20,0xa9,0xe6,0x4f,0x56,0x15,0xcd};#elif dmnqrjyzatnt(fjlctkcyasie)
qefbyeptiwaw mkvtbxldsaow[]={0x2b,0x7e,0x15,0x16,0x28,0xae,0xd2,0xa6,0xab,0xf7,0x15,0x88,0x09,0xcf,0x4f,0x3c};qefbyeptiwaw duvpfdojssqi[]={0x76,0x49,0xab,0xac,0x81,0x19,0xb2,0x46,0xce,0xe9,0x8e,0x9b,0x12,0xe9,0x19,0x7d,0x50,0x86,0xcb,0x9b,0x50,0x72,0x19,0xee,0x95,0xdb,0x11,0x3a,0x91,0x76,0x78,0xb2,0x73,0xbe,0xd6,0xb8,0xe3,0xc1,0x74,0x3b,0x71,0x16,0xe6,0x9e,0x22,0x22,0x95,0x16,0x3f,0xf1,0xca,0xa1,0x68,0x1f,0xac,0x09,0x12,0x0e,0xca,0x30,0x75,0x86,0xe1,0xa7};#endif
qefbyeptiwaw iv[]={0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b,0x0c,0x0d,0x0e,0x0f};qefbyeptiwaw pzmpgaimsysu[]={0x6b,0xc1,0xbe,0xe2,0x2e,0x40,0x9f,0x96,0xe9,0x3d,0x7e,0x11,0x73,0x93,0x17,0x2a,0xae,0x2d,0x8a,0x57,0x1e,0x03,0xac,0x9c,0x9e,0xb7,0x6f,0xac,0x45,0xaf,0x8e,0x51,0x30,0xc8,0x1c,0x46,0xa3,0x5c,0xe4,0x11,0xe5,0xfb,0xc1,0x19,0x1a,0x0a,0x52,0xef,0xf6,0x9f,0x24,0x45,0xdf,0x4f,0x9b,0x17,0xad,0x2b,0x41,0x7b,0xe6,0x6c,0x37,0x10};struct cikfasodieztctx;AES_init_ctx_iv(&ctx,mkvtbxldsaow,iv);AES_CBC_encrypt_buffer(&ctx,pzmpgaimsysu,64);bgpouftzlque("CBC encrypt: ");if(0==memcmp((rgvjzldlmjyn*)duvpfdojssqi,(rgvjzldlmjyn*)pzmpgaimsysu,64)){bgpouftzlque("SUCCESS!\n");return(0);}else {bgpouftzlque("FAILURE!\n");return(1);}}static yllaxbkvixtmilkkapemzpav(const rgvjzldlmjyn*xcrypt);static yllaxbkvixtmtest_encrypt_ctr(yvpwxqwmgcpg){return ilkkapemzpav("encrypt");}static yllaxbkvixtmtest_decrypt_ctr(yvpwxqwmgcpg){return ilkkapemzpav("decrypt");}static yllaxbkvixtmilkkapemzpav(const rgvjzldlmjyn*xcrypt){#if dmnqrjyzatnt(bqzttupqekuj)
qefbyeptiwaw mkvtbxldsaow[32]={0x60,0x3d,0xeb,0x10,0x15,0xca,0x71,0xbe,0x2b,0x73,0xae,0xf0,0x85,0x7d,0x77,0x81,0x1f,0x35,0x2c,0x07,0x3b,0x61,0x08,0xd7,0x2d,0x98,0x10,0xa3,0x09,0x14,0xdf,0xf4};qefbyeptiwaw pzmpgaimsysu[64]={0x60,0x1e,0xc3,0x13,0x77,0x57,0x89,0xa5,0xb7,0xa7,0xf5,0x04,0xbb,0xf3,0xd2,0x28,0xf4,0x43,0xe3,0xca,0x4d,0x62,0xb5,0x9a,0xca,0x84,0xe9,0x90,0xca,0xca,0xf5,0xc5,0x2b,0x09,0x30,0xda,0xa2,0x3d,0xe9,0x4c,0xe8,0x70,0x17,0xba,0x2d,0x84,0x98,0x8d,0xdf,0xc9,0xc5,0x8d,0xb6,0x7a,0xad,0xa6,0x13,0xc2,0xdd,0x08,0x45,0x79,0x41,0xa6};#elif dmnqrjyzatnt(ldchpcknctgz)
qefbyeptiwaw mkvtbxldsaow[24]={0x8e,0x73,0xb0,0xf7,0xda,0x0e,0x64,0x52,0xc8,0x10,0xf3,0x2b,0x80,0x90,0x79,0xe5,0x62,0xf8,0xea,0xd2,0x52,0x2c,0x6b,0x7b};qefbyeptiwaw pzmpgaimsysu[64]={0x1a,0xbc,0x93,0x24,0x17,0x52,0x1c,0xa2,0x4f,0x2b,0x04,0x59,0xfe,0x7e,0x6e,0x0b,0x09,0x03,0x39,0xec,0x0a,0xa6,0xfa,0xef,0xd5,0xcc,0xc2,0xc6,0xf4,0xce,0x8e,0x94,0x1e,0x36,0xb2,0x6b,0xd1,0xeb,0xc6,0x70,0xd1,0xbd,0x1d,0x66,0x56,0x20,0xab,0xf7,0x4f,0x78,0xa7,0xf6,0xd2,0x98,0x09,0x58,0x5a,0x97,0xda,0xec,0x58,0xc6,0xb0,0x50};#elif dmnqrjyzatnt(fjlctkcyasie)
qefbyeptiwaw mkvtbxldsaow[16]={0x2b,0x7e,0x15,0x16,0x28,0xae,0xd2,0xa6,0xab,0xf7,0x15,0x88,0x09,0xcf,0x4f,0x3c};qefbyeptiwaw pzmpgaimsysu[64]={0x87,0x4d,0x61,0x91,0xb6,0x20,0xe3,0x26,0x1b,0xef,0x68,0x64,0x99,0x0d,0xb6,0xce,0x98,0x06,0xf6,0x6b,0x79,0x70,0xfd,0xff,0x86,0x17,0x18,0x7b,0xb9,0xff,0xfd,0xff,0x5a,0xe4,0xdf,0x3e,0xdb,0xd5,0xd3,0x5e,0x5b,0x4f,0x09,0x02,0x0d,0xb0,0x3e,0xab,0x1e,0x03,0x1d,0xda,0x2f,0xbe,0x03,0xd1,0x79,0x21,0x70,0xa0,0xf3,0x00,0x9c,0xee};#endif
qefbyeptiwaw iv[16]={0xf0,0xf1,0xf2,0xf3,0xf4,0xf5,0xf6,0xf7,0xf8,0xf9,0xfa,0xfb,0xfc,0xfd,0xfe,0xff};qefbyeptiwaw duvpfdojssqi[64]={0x6b,0xc1,0xbe,0xe2,0x2e,0x40,0x9f,0x96,0xe9,0x3d,0x7e,0x11,0x73,0x93,0x17,0x2a,0xae,0x2d,0x8a,0x57,0x1e,0x03,0xac,0x9c,0x9e,0xb7,0x6f,0xac,0x45,0xaf,0x8e,0x51,0x30,0xc8,0x1c,0x46,0xa3,0x5c,0xe4,0x11,0xe5,0xfb,0xc1,0x19,0x1a,0x0a,0x52,0xef,0xf6,0x9f,0x24,0x45,0xdf,0x4f,0x9b,0x17,0xad,0x2b,0x41,0x7b,0xe6,0x6c,0x37,0x10};struct cikfasodieztctx;AES_init_ctx_iv(&ctx,mkvtbxldsaow,iv);AES_CTR_xcrypt_buffer(&ctx,pzmpgaimsysu,64);bgpouftzlque("CTR %s: ",xcrypt);if(0==memcmp((rgvjzldlmjyn *)duvpfdojssqi,(rgvjzldlmjyn *)pzmpgaimsysu,64)){bgpouftzlque("SUCCESS!\n");return(0);}else {bgpouftzlque("FAILURE!\n");return(1);}}static yllaxbkvixtmtest_decrypt_ecb(yvpwxqwmgcpg){#if dmnqrjyzatnt(bqzttupqekuj)
qefbyeptiwaw mkvtbxldsaow[]={0x60,0x3d,0xeb,0x10,0x15,0xca,0x71,0xbe,0x2b,0x73,0xae,0xf0,0x85,0x7d,0x77,0x81,0x1f,0x35,0x2c,0x07,0x3b,0x61,0x08,0xd7,0x2d,0x98,0x10,0xa3,0x09,0x14,0xdf,0xf4};qefbyeptiwaw pzmpgaimsysu[]={0xf3,0xee,0xd1,0xbd,0xb5,0xd2,0xa0,0x3c,0x06,0x4b,0x5a,0x7e,0x3d,0xb1,0x81,0xf8};#elif dmnqrjyzatnt(ldchpcknctgz)
qefbyeptiwaw mkvtbxldsaow[]={0x8e,0x73,0xb0,0xf7,0xda,0x0e,0x64,0x52,0xc8,0x10,0xf3,0x2b,0x80,0x90,0x79,0xe5,0x62,0xf8,0xea,0xd2,0x52,0x2c,0x6b,0x7b};qefbyeptiwaw pzmpgaimsysu[]={0xbd,0x33,0x4f,0x1d,0x6e,0x45,0xf2,0x5f,0xf7,0x12,0xa2,0x14,0x57,0x1f,0xa5,0xcc};#elif dmnqrjyzatnt(fjlctkcyasie)
qefbyeptiwaw mkvtbxldsaow[]={0x2b,0x7e,0x15,0x16,0x28,0xae,0xd2,0xa6,0xab,0xf7,0x15,0x88,0x09,0xcf,0x4f,0x3c};qefbyeptiwaw pzmpgaimsysu[]={0x3a,0xd7,0x7b,0xb4,0x0d,0x7a,0x36,0x60,0xa8,0x9e,0xca,0xf3,0x24,0x66,0xef,0x97};#endif
qefbyeptiwaw duvpfdojssqi[]={0x6b,0xc1,0xbe,0xe2,0x2e,0x40,0x9f,0x96,0xe9,0x3d,0x7e,0x11,0x73,0x93,0x17,0x2a};struct cikfasodieztctx;AES_init_ctx(&ctx,mkvtbxldsaow);AES_ECB_decrypt(&ctx,pzmpgaimsysu);bgpouftzlque("ECB decrypt: ");if(0==memcmp((rgvjzldlmjyn*)duvpfdojssqi,(rgvjzldlmjyn*)pzmpgaimsysu,16)){bgpouftzlque("SUCCESS!\n");return(0);}else {bgpouftzlque("FAILURE!\n");return(1);}}